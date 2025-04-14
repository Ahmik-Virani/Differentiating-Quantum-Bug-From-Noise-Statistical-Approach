from __future__ import print_function
import random
import os
import platform
import subprocess
import sys
import json

# Assuming QuantumGates is in your module search path. Adjust if necessary.
from . import QuantumGates

def createMutants(maxNum, operators, types, gateIDs, locationIDs, originPath, savePath, all_mutations, phases):
    maxNum=20
    '''
    if all_mutations:
        info = getInfo(originPath)
        operators = ("Add", "Remove", "Replace")
        types = ("OneQubit", "ManyQubit")
        x = 1
        gateIDs = (x,)
        while x < info[2]:
            x = x + 1
            gateIDs = gateIDs + (x,)

        x = 1
        locationIDs = (x,)
        # Using info[2] for TotalGateNum and info[0] for QubitNum
        while x < (info[2] + info[0]):
            x = x + 1
            locationIDs = locationIDs + (x,)
        maxNum = len(QuantumGates.AllGates) * len(locationIDs) + (len(QuantumGates.AllGates) - 1) * len(gateIDs) + len(gateIDs)'''
    
    gateNum = len(gateIDs)
    locationsLenght = len(locationIDs)
    restquantity = maxNum
    first = True
    totalMutants = 0

    # Group only selected type gates.
    if "OneQubit" in types:
        if "ManyQubit" in types:
            gates = QuantumGates.AllGates
        else:
            gates = QuantumGates.OneQubit
    elif "ManyQubit" in types:
        gates = QuantumGates.TwoQubit + QuantumGates.MoreThanTwoQubit

    # Call each operator if selected.
    if "Add" in operators:
        num = restquantity // len(operators)
        rest = restquantity % len(operators)
        addnum = num + rest
        if addnum > locationsLenght * len(gates):
            addnum = locationsLenght * len(gates)
        if all_mutations:
            addnum = locationsLenght * len(gates)
        restquantity = restquantity - addnum
        totalMutants = totalMutants + add(addnum, gates, locationIDs, originPath, savePath, phases)
        first = False
    if "Remove" in operators:
        if first:
            num = restquantity // len(operators)
            rest = restquantity % len(operators)
            removenum = num + rest
            if removenum > gateNum:
                removenum = gateNum
            if all_mutations:
                removenum = gateNum
            restquantity = restquantity - removenum
            totalMutants = totalMutants + remove(removenum, gates, gateIDs, originPath, savePath)
        else:
            removenum = restquantity // (len(operators) - 1)
            if removenum > gateNum:
                removenum = gateNum
            if all_mutations:
                removenum = gateNum
            restquantity = restquantity - removenum
            totalMutants = totalMutants + remove(removenum, gates, gateIDs, originPath, savePath)
    if "Replace" in operators:
        replacenum = restquantity
        if replacenum > (gateNum * len(gates)) - gateNum:
            replacenum = (gateNum * len(gates)) - gateNum
        if all_mutations:
            replacenum = (gateNum * len(gates)) - gateNum
        totalMutants = totalMutants + replace(replacenum, gates, gateIDs, originPath, savePath, phases)

    print("Number of mutants created: " + str(totalMutants))
    '''
    mutants_per_operator = 10
    totalMutants = 0

    # Group the gates based on the selected types.
    if "OneQubit" in types:
        if "ManyQubit" in types:
            gates = QuantumGates.AllGates
        else:
            gates = QuantumGates.OneQubit
    elif "ManyQubit" in types:
        gates = QuantumGates.TwoQubit + QuantumGates.MoreThanTwoQubit
    else:
        # Fallback if no type is selected.
        gates = QuantumGates.AllGates

    # For each operator, create only one mutant.
    if "Add" in operators:
        totalMutants += add(mutants_per_operator, gates, locationIDs, originPath, savePath, phases)
    if "Remove" in operators:
        totalMutants += remove(mutants_per_operator, gates, gateIDs, originPath, savePath)
    if "Replace" in operators:
        totalMutants += replace(mutants_per_operator, gates, gateIDs, originPath, savePath, phases)

    print("Number of mutants created: " + str(totalMutants))
'''
def createInputs(QubitNum):
    inputs = ("",)
    x = 0
    while x < 2 ** QubitNum:
        binariInput = str(bin(x))[2:]
        if len(binariInput) < QubitNum:
            tmp = "0" * (QubitNum - len(binariInput))
            binariInput = tmp + binariInput
        inputs = inputs + (binariInput,)
        x = x + 1
    return inputs[1:]


def simulate_original_circuit(file, numShots, info):
    """
    Simulate the original (unmutated) circuit.
    Writes a temporary file that:
      - Imports necessary modules,
      - Loads the original circuit,
      - Appends measurement instructions,
      - Simulates the circuit using AerSimulator,
      - Prints the counts as JSON.
      
    The printed JSON is captured and returned as a dictionary.
    """
    QubitNum, CircuitName, QubitGateNum, QubitName, ClassicName, _ = info
    tmp_original = os.path.join(os.path.dirname(file), "tmp_original.py")
    with open(file, 'r') as src, open(tmp_original, 'w') as dst:
        # Write required imports.
        dst.write("import json\n")
        dst.write("from qiskit_aer import AerSimulator\n")
        dst.write("from qiskit import transpile\n")
        dst.write("\n")
        # Copy original file contents.
        for line in src:
            dst.write(line)
        dst.write("\n")
        # Append measurement instructions for all qubits.
        for y in range(QubitNum):
            dst.write(f"{CircuitName}.measure({QubitName}[{y}], {ClassicName}[{y}])\n")
        dst.write("\n")
        # Append simulation code that prints counts as JSON.
        dst.write("simulator = AerSimulator()\n")
        dst.write(f"{CircuitName} = transpile({CircuitName}, simulator)\n")
        dst.write(f"job = simulator.run({CircuitName}, shots={numShots})\n")
        dst.write("result = job.result()\n")
        dst.write(f"counts = result.get_counts({CircuitName})\n")
        dst.write("print(json.dumps(counts))\n")
    
    venv_python = sys.executable
    command = [venv_python, tmp_original]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        counts = json.loads(result.stdout.strip())
    except Exception as e:
        print("Error during original circuit simulation:", e)
        counts = {}
    finally:
        if os.path.exists(tmp_original):
            os.remove(tmp_original)
    return counts


def executeMutants(files_dir, resultPath, numShots, allInputs, inputs):
    """
    Processes each mutant circuit in a given directory:
      1. Extracts information about the circuit.
      2. Simulates the original (unmutated) circuit to obtain its golden output
         (reference counts).
      3. For a specified input scenario:
         - Reads the mutant file.
         - Injects extra instructions (e.g., X gates based on the init string).
         - Writes a temporary script that:
              * Imports needed modules.
              * Defines the variable 'original_counts' (by inlining its JSON representation),
              * Appends measurement instructions,
              * Simulates the circuit,
              * Computes bias based on comparing mutant counts with the original counts.
         - Executes the temporary script.
         - Appends the calculated bias value to the result file.
         If an error occurs during execution of the temporary script, "0.000," is written.
    """
    import os, subprocess, json

    print(files_dir)
    original_file_name = "Testcases/deep/" + files_dir[len("Mutants/deep/mutants_of_"):] + ".py"
    print(original_file_name)
    # Ensure the result directory exists.
    result_dir = os.path.dirname(resultPath)
    if result_dir and not os.path.exists(result_dir):
        os.makedirs(result_dir, exist_ok=True)

    # Use a temporary file (path) to store and run the generated script.
    tmpPath = os.path.join(result_dir, "tmp.py")

    # Get list of mutant files (full paths)
    mutant_files = [
        os.path.join(files_dir, f)
        for f in os.listdir(files_dir)
        if os.path.isfile(os.path.join(files_dir, f))
    ]

    for file in mutant_files:
        try:
            print("Processing mutant file:", file)
            # Extract necessary circuit information; assuming getInfo returns:
            # (QubitNum, CircuitName, QubitGateNum, QubitName, ClassicName, other_info)
            info = getInfo(file)
            QubitNum = info[0]
            CircuitName = info[1]
            QubitName = info[3]
            ClassicName = info[4]

            # Simulate the unmodified original circuit and obtain its counts.
            original_counts = simulate_original_circuit(original_file_name, numShots, getInfo(original_file_name))
            print("Original counts:", original_counts)

            # If allInputs flag is set, generate all input strings.
            if allInputs:
                inputs = createInputs(QubitNum)
            # Instead of looping over all inputs, only use the first input scenario.
            init = inputs[0]

            with open(file, 'r') as f, open(tmpPath, 'w') as g:
                # Write required imports.
                g.write("import json\n")
                g.write("from qiskit_aer import AerSimulator\n")
                g.write("from qiskit import transpile\n")
                g.write("\n")
                # Inject the original_counts variable definition into the temporary file.
                g.write("original_counts = " + json.dumps(original_counts) + "\n")
                g.write("\n")
                # Copy contents of the mutant file.
                for line in f:
                    g.write(line)
                    # Look for a line that includes "QuantumCircuit" to inject extra instructions.
                    if "QuantumCircuit" in line:
                        g.write("\n")
                        # For each bit in the input string, inject an X gate if that bit is '1'.
                        for z, bit in enumerate(init, start=1):
                            if bit == "1":
                                # Compute the index for the qubit; adjust as needed.
                                g.write(f"{CircuitName}.x({QubitName}[{QubitNum - z}])\n")
                g.write("\n")
                # Append measurement instructions for all qubits.
                for y in range(QubitNum):
                    g.write(f"{CircuitName}.measure({QubitName}[{y}], {ClassicName}[{y}])\n")
                g.write("\n")
                # Append simulation and bias calculation code.
                g.write(f"""
def calculate_bias(output_map, unwanted_states):
    total_count = sum(output_map.values())
    bias = 0
    for key, val in output_map.items():
        if key in unwanted_states:
            bias += val / total_count
    return bias

simulator = AerSimulator()
{CircuitName} = transpile({CircuitName}, simulator)
job = simulator.run({CircuitName}, shots={numShots})
result = job.result()
mutant_counts = result.get_counts({CircuitName})
print("Mutant counts:", mutant_counts)

def generate_all_possible_outcomes(num_qubits):
    return [format(i, '0' + str(num_qubits) + 'b') for i in range(2**num_qubits)]
all_possible = generate_all_possible_outcomes({QubitNum})
# Define unwanted states as outcomes not present in original_counts.
unwanted_states = set(all_possible) - set(original_counts.keys())
bias = calculate_bias(mutant_counts, unwanted_states)
print("Calculated bias:", bias)
with open(r"{resultPath}", "a") as r:
    r.write(f"{{bias:.4f}},")
""")
            # Execute the generated temporary file.
            venv_python = sys.executable
            command = [venv_python, tmpPath]
            try:
                subprocess.run(command, check=True, env=os.environ.copy())
            except subprocess.CalledProcessError:
                with open(resultPath, "a") as r:
                    r.write("-0.000,")
        except Exception as e:
            print(f"Error processing {file}: {str(e)}")

    # Clean up the temporary file if it still exists.
    if os.path.exists(tmpPath):
        os.remove(tmpPath)





def add(max, gateTypes, locations, origin, dirPath, phases):
    splitChar = 92
    if chr(splitChar) not in origin:
        splitChar = 47
    os.makedirs(dirPath, exist_ok=True)
    Info = getInfo(origin)
    QubitNum = Info[0]
    CircuitName = Info[1]
    TotalGateNum = Info[2]
    QubitName = Info[3]
    MutationNum = 0
    CurrentGate = 0
    ObjectiveGap = 0
    while ObjectiveGap not in locations:
        ObjectiveGap = ObjectiveGap + 1
    while MutationNum < max:
        CurrentGap = 0
        Mutated = False
        MutationNum = MutationNum + 1
        newPath = dirPath + chr(splitChar) + str(MutationNum) + "AddGate_" + str(gateTypes[CurrentGate]) + "_inGap_" + str(
            ObjectiveGap) + "_.py"
        f = open(origin)
        g = open(newPath, "w")
        line = f.readline()
        while line != "":
            if ((CircuitName in line) and ("QuantumCircuit" not in line) and (Mutated is False)):
                temp = line.split(".",1)
                temp2 = temp[1].split("(")
                if ObjectiveGap > TotalGateNum:
                    temp2 = QubitName + "[" + str(ObjectiveGap - TotalGateNum - 1) + "]"
                if temp2[0] in QuantumGates.AllGates:
                    CurrentGap = CurrentGap + 1
                    if CurrentGap == ObjectiveGap:
                        if gateTypes[CurrentGate] in QuantumGates.TwoQubit or gateTypes[CurrentGate] in QuantumGates.MoreThanTwoQubit:
                            if gateTypes[CurrentGate] in QuantumGates.MoreThanTwoQubit:
                                if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                    temp3 = temp2[1].split(",")
                                    temp4 = temp3[len(temp3) - 1].split("[")
                                    temp4 = temp4[1].split("]")
                                    num = int(temp4[0])
                                    if num == QubitNum - 1:
                                        num1 = num - 1
                                        num2 = num - 2
                                    elif num == QubitNum - 2:
                                        num1 = num + 1
                                        num2 = num - 1
                                    else:
                                        num1 = num + 1
                                        num2 = num + 2
                                    g.write(
                                        str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                                            phases[
                                                random.randint(0, len(phases) - 1)]) + ", " + str(
                                            QubitName) + "[" + str(num1) + "]" + ", " + str(
                                            QubitName) + "[" + str(num2) + "]" + ", " + str(temp3[len(temp3) - 1]))
                                    Mutated = True
                                else:
                                    temp3 = temp2[1].split(",")
                                    temp4 = temp3[len(temp3) - 1].split("[")
                                    temp4 = temp4[1].split("]")
                                    num = int(temp4[0])

                                    if num == QubitNum - 1:
                                        num1 = num - 1
                                        num2 = num - 2
                                    elif num == QubitNum - 2:
                                        num1 = num + 1
                                        num2 = num - 1
                                    else:
                                        num1 = num + 1
                                        num2 = num + 2
                                    g.write(
                                        str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                                            QubitName) + "[" + str(num1) + "]" + ", " + str(
                                            QubitName) + "[" + str(num2) + "]" + ", " + str(temp3[len(temp3) - 1]))
                                    Mutated = True
                            else:
                                if temp2[0] in QuantumGates.MoreThanTwoQubit:
                                    tmp = temp2[1].split(",",1)
                                    temp2[1] = tmp[1]
                                if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                    if temp2[0] in QuantumGates.TwoQubit:
                                        if temp2[0] in QuantumGates.PhaseGates:
                                            temp3 = temp2[1].split(",", 1)
                                            g.write(str(CircuitName) + "." + str(
                                                gateTypes[CurrentGate]) + "(" + str(phases[
                                                                                        random.randint(0, len(
                                                                                            phases) - 1)]) + "," + str(
                                                temp3[1]))
                                            Mutated = True
                                        else:
                                            g.write(str(CircuitName) + "." + str(
                                                gateTypes[CurrentGate]) + "(" + str(phases[
                                                                                        random.randint(0, len(
                                                                                            phases) - 1)]) + "," + str(
                                                temp2[1]))
                                            Mutated = True
                                    else:
                                        temp3 = temp2[1].split(",")
                                        temp4 = temp3[len(temp3) - 1].split("[")
                                        temp4 = temp4[1].split("]")
                                        num = int(temp4[0])
                                        if num == QubitNum - 1:
                                            num = num - 1
                                        else:
                                            num = num + 1
                                        g.write(
                                            str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                                                phases[
                                                    random.randint(0, len(phases) - 1)]) + ", " + str(
                                                QubitName) + "[" + str(num) + "]" ", " + str(temp3[len(temp3) - 1]))
                                        Mutated = True

                                else:
                                    if temp2[0] in QuantumGates.TwoQubit:
                                        if temp2[0] in QuantumGates.PhaseGates:
                                            temp3 = temp2[1].split(",", 1)
                                            g.write(str(CircuitName) + "." + str(
                                                gateTypes[CurrentGate]) + "(" + str(temp3[1]))
                                            Mutated = True
                                        else:
                                            g.write(str(CircuitName) + "." + str(
                                                gateTypes[CurrentGate]) + "(" + str(temp2[1]))
                                            Mutated = True
                                    else:
                                        temp3 = temp2[1].split(",")
                                        temp4 = temp3[len(temp3) - 1].split("[")
                                        temp4 = temp4[1].split("]")
                                        num = int(temp4[0])
                                        if num == QubitNum - 1:
                                            num = num - 1
                                        else:
                                            num = num + 1
                                        g.write(
                                            str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                                                QubitName) + "[" + str(num) + "]" ", " + str(temp3[len(temp3) - 1]))
                                        Mutated = True
                        else:
                            if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                temp3 = temp2[1].split(",")
                                g.write(
                                    str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                                        phases[
                                            random.randint(0, len(phases) - 1)]) + "," + str(
                                        temp3[len(temp3) - 1]))
                                Mutated = True
                            else:
                                temp3 = temp2[1].split(",")
                                g.write(str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                                    temp3[len(temp3) - 1]))
                                Mutated = True
            g.write(line)
            line = f.readline()
            if Mutated is False and line == "":
                qubit = ObjectiveGap - TotalGateNum - 1
                if qubit == QubitNum - 1:
                    qubit2 = qubit - 1
                else:
                    qubit2 = qubit + 1
                if gateTypes[CurrentGate] in QuantumGates.TwoQubit or gateTypes[CurrentGate] in QuantumGates.MoreThanTwoQubit:
                    if gateTypes[CurrentGate] in QuantumGates.MoreThanTwoQubit:
                        if qubit == QubitNum - 2:
                            qubit3 = qubit - 1
                        elif qubit == QubitNum - 1:
                            qubit3 = qubit - 2
                        else:
                            qubit3 = qubit + 2

                        if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                            g.write(
                                str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                                    phases[
                                        random.randint(0, len(phases) - 1)]) + ", " + str(
                                    QubitName) + "[" + str(qubit2) + "]" + ", " + str(
                                    QubitName) + "[" + str(qubit3) + "]" + ", " + str(
                                    QubitName) + "[" + str(qubit) + "])")
                            Mutated = True
                        else:

                            g.write(
                                str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                                    QubitName) + "[" + str(qubit2) + "]" + ", " + str(
                                    QubitName) + "[" + str(qubit3) + "]" + ", " + str(
                                    QubitName) + "[" + str(qubit) + "])")
                            Mutated = True
                    else:
                        if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                            g.write("\n")
                            g.write(str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(phases[random.randint(0, len(phases) - 1)]) + "," + str(QubitName) + "[" + str(qubit2) + "]" + "," + str(QubitName) + "[" + str(qubit) + "]" + ")")
                            Mutated = True
                        else:
                            g.write("\n")
                            g.write(str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(QubitName) + "[" + str(qubit2) + "]" + "," + str(QubitName) + "[" + str(qubit) + "]" + ")")
                            Mutated = True
                else:
                    if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                        g.write("\n")
                        g.write(str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                            phases[random.randint(0, len(phases) - 1)]) + "," + str(
                            QubitName) + "[" + str(
                            qubit) + "]" + ")")
                        Mutated = True
                    else:
                        g.write("\n")
                        g.write(str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(QubitName) + "[" + str(
                            qubit) + "]" + ")")
                        Mutated = True

        f.close()
        g.close()
        if CurrentGate >= len(gateTypes) - 1:
            ObjectiveGap = ObjectiveGap + 1
            while (ObjectiveGap not in locations) and (ObjectiveGap < locations[(len(locations) - 1)]):
                ObjectiveGap = ObjectiveGap + 1
            CurrentGate = 0
        else:
            CurrentGate = CurrentGate + 1

    print("The ADD mutated files are located in: " + dirPath)
    return MutationNum


def replace(num, gateTypes, changeGates, origin, dirPath, phases):
    splitChar = 92
    if chr(splitChar) not in origin:
        splitChar = 47
    # dirPath = dirPath + chr(splitChar) + "ReplaceMutations"
    os.makedirs(dirPath, exist_ok=True)

    Info = getInfo(origin)
    CircuitName = Info[1]
    MutationNum = 0
    CurrentGate = 0
    ObjectiveGap = 0
    while ObjectiveGap not in changeGates:
        ObjectiveGap = ObjectiveGap + 1
    while MutationNum < num:
        delete = False
        CurrentGap = 0
        Mutated = False
        MutationNum = MutationNum + 1
        newPath = dirPath + chr(splitChar) + str(MutationNum) + "ReplaceGate.py"
        f = open(origin)
        g = open(newPath, "w")
        line = f.readline()
        while line != "":
            if (CircuitName in line) and ("QuantumCircuit" not in line) and (Mutated is False):
                temp = line.split(".",1)
                temp2 = temp[1].split("(")
                if temp2[0] in gateTypes:
                    CurrentGap = CurrentGap + 1
                    if CurrentGap == ObjectiveGap and (CurrentGap in changeGates):
                        if gateTypes[CurrentGate] == temp2[0]:
                            CurrentGate = CurrentGate + 1
                            if CurrentGate >= len(gateTypes):
                                ObjectiveGap = ObjectiveGap + 1
                                while (ObjectiveGap not in changeGates) and (
                                        ObjectiveGap < changeGates[(len(changeGates) - 1)]):
                                    ObjectiveGap = ObjectiveGap + 1

                                if ObjectiveGap > changeGates[(len(changeGates)-1)]:
                                    delete = True
                                CurrentGate = 0
                        if CurrentGap == ObjectiveGap:
                            if temp2[0] in QuantumGates.MoreThanTwoQubit or gateTypes[CurrentGate] in QuantumGates.MoreThanTwoQubit:
                                if temp2[0] in QuantumGates.MoreThanTwoQubit and gateTypes[CurrentGate] in QuantumGates.MoreThanTwoQubit:
                                    if temp2[0] in QuantumGates.PhaseGates:
                                        if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                            g.write(
                                                str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp2[1]))
                                            Mutated = True
                                        else:
                                            temp3 = temp2[1].split(",",1)
                                            g.write(
                                                str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp3[1]))
                                            Mutated = True
                                    else:
                                        if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                            g.write(
                                                str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(phases[random.randint(0, len(phases) - 1)]) + ", " + str(temp2[1]))
                                            Mutated = True
                                        else:
                                            g.write(
                                                str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp2[1]))
                                            Mutated = True
                                else:
                                    if temp2[0] in QuantumGates.MoreThanTwoQubit:
                                        while gateTypes[CurrentGate] not in QuantumGates.MoreThanTwoQubit:
                                            CurrentGate = CurrentGate + 1
                                        if gateTypes[CurrentGate] == temp2[0]:
                                            CurrentGate = CurrentGate + 1
                                            if CurrentGate >= len(gateTypes):
                                                ObjectiveGap = ObjectiveGap + 1
                                                while (ObjectiveGap not in changeGates) and (
                                                        ObjectiveGap < changeGates[(len(changeGates) - 1)]):
                                                    ObjectiveGap = ObjectiveGap + 1

                                                if ObjectiveGap > changeGates[(len(changeGates) - 1)]:
                                                    delete = True
                                                CurrentGate = 0
                                                g.write(line)
                                        else:
                                            if temp2[0] in QuantumGates.PhaseGates:
                                                if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                                    g.write(
                                                        str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                                                            temp2[1]))
                                                    Mutated = True
                                                else:
                                                    temp3 = temp2[1].split(",", 1)
                                                    g.write(
                                                        str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                                                            temp3[1]))
                                                    Mutated = True
                                            else:
                                                if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                                    g.write(
                                                        str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                                                            phases[random.randint(0, len(
                                                                phases) - 1)]) + ", " + str(temp2[1]))
                                                    Mutated = True
                                                else:
                                                    g.write(
                                                        str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(
                                                            temp2[1]))
                                                    Mutated = True
                                    else:
                                        ObjectiveGap = ObjectiveGap + 1
                                        while (ObjectiveGap not in changeGates) and (
                                                ObjectiveGap < changeGates[(len(changeGates) - 1)]):
                                            ObjectiveGap = ObjectiveGap + 1

                                        if ObjectiveGap > changeGates[(len(changeGates) - 1)]:
                                            delete = True
                                        CurrentGate=0
                                        g.write(line)

                            else:
                                if temp2[0] in QuantumGates.TwoQubit or gateTypes[CurrentGate] in QuantumGates.TwoQubit:
                                    if temp2[0] in QuantumGates.TwoQubit and gateTypes[CurrentGate] in QuantumGates.TwoQubit:
                                        if temp2[0] in QuantumGates.PhaseGates:
                                            if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                                g.write(
                                                    str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp2[1]))
                                                Mutated = True
                                            else:
                                                temp3 = temp2[1].split(",")
                                                g.write(
                                                    str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp3[1]))
                                                Mutated = True
                                        else:
                                            if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                                g.write(str(CircuitName) + "." + str(gateTypes[CurrentGate]) +
                                                "(" + str(phases[random.randint(0, len(phases) - 1)]) + "," + str(temp2[1]))
                                                Mutated = True
                                            else:
                                                g.write(
                                                    str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp2[1]))
                                                Mutated = True
                                    else:
                                        if temp2[0] in QuantumGates.TwoQubit:
                                            while gateTypes[CurrentGate] not in QuantumGates.TwoQubit:
                                                CurrentGate = CurrentGate + 1
                                            if gateTypes[CurrentGate] == temp2[0]:
                                                CurrentGate = CurrentGate + 1
                                            if temp2[0] in QuantumGates.PhaseGates:
                                                if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                                    g.write(
                                                        str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp2[1]))
                                                    Mutated = True
                                                else:
                                                    temp3 = temp2[1].split(",")
                                                    qubits = temp3[1]
                                                    for x in temp3:
                                                        if x != temp3[0] and x != temp3[1]:
                                                            qubits = qubits + "," + x
                                                    g.write(
                                                        str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(qubits))
                                                    Mutated = True
                                            else:
                                                if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                                    g.write(str(CircuitName) + "." + str(gateTypes[CurrentGate]) +
                                                    "(" + str(phases[random.randint(0, len(phases) - 1)]) + "," + str(temp2[1]))
                                                    Mutated = True
                                                else:
                                                    g.write(
                                                        str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp2[1]))
                                                    Mutated = True
                                        else:
                                            CurrentGap = CurrentGap + 1
                                            CurrentGate = 0

                                else:
                                    if temp2[0] in QuantumGates.PhaseGates:
                                        if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                            g.write(
                                                str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp2[1]))
                                            Mutated = True
                                        else:
                                            temp3 = temp2[1].split(",")
                                            g.write(
                                                str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp3[1]))
                                            Mutated = True
                                    else:
                                        if gateTypes[CurrentGate] in QuantumGates.PhaseGates:
                                            g.write(str(CircuitName) + "." + str(gateTypes[CurrentGate]) +
                                            "(" + str(phases[random.randint(0, len(phases) - 1)]) + "," + str(temp2[1]))
                                            Mutated = True
                                        else:
                                            g.write(
                                                str(CircuitName) + "." + str(gateTypes[CurrentGate]) + "(" + str(temp2[1]))
                                            Mutated = True
                                    if CurrentGate < len(gateTypes)-1:
                                        if gateTypes[CurrentGate+1] in QuantumGates.TwoQubit:
                                            ObjectiveGap = ObjectiveGap + 1
                                            while (ObjectiveGap not in changeGates) and (
                                                    ObjectiveGap < changeGates[(len(changeGates) - 1)]):
                                                ObjectiveGap = ObjectiveGap + 1
                                            CurrentGate = -1
                        else:
                            g.write(line)
                    else:
                        g.write(line)
            else:
                g.write(line)
            line = f.readline()

        f.close()
        g.close()
        if Mutated == False or delete == True:
            os.remove(newPath)
            MutationNum = MutationNum - 1
            CurrentGate = CurrentGate - 1
        if CurrentGate == len(gateTypes) - 1:
            ObjectiveGap = ObjectiveGap + 1
            while (ObjectiveGap not in changeGates) and (ObjectiveGap < changeGates[(len(changeGates) - 1)]):
                ObjectiveGap = ObjectiveGap + 1
            CurrentGate = 0
        else:
            CurrentGate = CurrentGate + 1
        total = MutationNum
        if ObjectiveGap > changeGates[(len(changeGates) - 1)]:
            MutationNum = num

    print("The REPLACE mutated files are located in: " + dirPath)
    return total

def remove(num, gateTypes, changeGates, origin, dirPath):
    splitChar = 92
    if chr(splitChar) not in origin:
        splitChar = 47
    os.makedirs(dirPath, exist_ok=True)

    Info = getInfo(origin)
    CircuitName = Info[1]
    MutationNum = 0
    ObjectiveGap = 0
    while ObjectiveGap not in changeGates:
        ObjectiveGap = ObjectiveGap + 1
    while MutationNum < num:
        CurrentGap = 0
        Mutated = False
        MutationNum = MutationNum + 1
        newPath = dirPath + chr(splitChar) + "RemoveGate_" + str(ObjectiveGap) + "_.py"
        f = open(origin)
        g = open(newPath, "w")
        line = f.readline()
        while line != "":
            if (CircuitName in line) and ("QuantumCircuit" not in line) and (Mutated is False):
                temp = line.split(".", 1)
                temp2 = temp[1].split("(")
                if temp2[0] in gateTypes:
                    CurrentGap = CurrentGap + 1
                    if CurrentGap == ObjectiveGap and (CurrentGap in changeGates):
                        Mutated = True
                    else:
                        g.write(line)
                else:
                    g.write(line)
            else:
                g.write(line)
            line = f.readline()
        f.close()
        g.close()
        ObjectiveGap = ObjectiveGap + 1
        while (ObjectiveGap not in changeGates) and (ObjectiveGap < changeGates[(len(changeGates)-1)]):
            ObjectiveGap = ObjectiveGap + 1
    print("The REMOVE mutated files are located in: " + dirPath)
    return MutationNum


def getInfo(origin):
    x = 0
    gates = ("",)
    f = open(origin)
    line = f.readline()
    GateNum = 0
    CircuitName = "Null"
    QubitName = "Null"
    ClasicName = "Null"
    QubitNum = 0
    while line != "":
        if "QuantumRegister(" in line:
            temp = line.split("(")
            temp2 = temp[1].split(",")
            temp2 = temp2[0].split(")")
            temp3 = temp[0].split(" ")
            QubitName = temp3[0]
            QubitNum = int(temp2[0])
        elif "QuantumCircuit(" in line:
            temp = line.split(" ")
            CircuitName = temp[0]
        elif (CircuitName in line) and CircuitName != "Null":
            temp = line.split(".", 1)
            temp2 = temp[1].split("(")
            temp3 = temp2[1].split("[")
            temp4 = temp3[len(temp3) - 1].split("]")
            if temp2[0] in QuantumGates.AllGates:
                GateNum = GateNum + 1
                gate = str(GateNum) + " Gate: " + temp2[0] + " in Qubit " + temp4[0]
                if GateNum == 1:
                    gates = (gate,)
                else:
                    gates = gates + (gate,)
        elif "ClassicalRegister(" in line:
            temp = line.split(" ")
            ClasicName = temp[0]
        line = f.readline()
    while x < QubitNum:
        gates = gates + (((str(GateNum + x + 1) + " Qubit " + str(x)) + " Last Gap"),)
        x = x + 1
    f.close()
    return QubitNum, CircuitName, GateNum, QubitName, ClasicName, gates
