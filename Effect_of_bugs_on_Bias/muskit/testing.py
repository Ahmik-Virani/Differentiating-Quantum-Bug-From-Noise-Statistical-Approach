import random
import math
import os
import subprocess
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def generate_random_qiskit_circuit(num_qubits, num_operations, filename):
    code = f"""import math
from qiskit import *

q = QuantumRegister({num_qubits}, 'q')
c = ClassicalRegister({num_qubits}, 'c')
qc = QuantumCircuit(q, c)

"""
    
    gates = ["x", "h", "p", "t", "s", "z", "y", "id", "rx", "ry", "rz", "sx", "swap", "rzz", "rxx", "cx", "cz", "ccx", "cswap"]
    
    for _ in range(num_operations):
        gate = random.choice(gates)
        
        if gate in ['x', 'h', 't', 's', 'z', 'y', 'id', 'sx']:
            qubit = random.randint(0, num_qubits - 1)
            code += f"qc.{gate}(q[{qubit}])\n"
        elif gate in ['p', 'rx', 'ry', 'rz']:
            qubit = random.randint(0, num_qubits - 1)
            angle = random.uniform(0, 2*math.pi)
            code += f"qc.{gate}(math.pi/{int(2*math.pi/angle)}, q[{qubit}])\n"
        elif gate in ['cx', 'cz', 'swap']:
            control = random.randint(0, num_qubits - 1)
            target = random.randint(0, num_qubits - 1)
            while target == control:
                target = random.randint(0, num_qubits - 1)
            code += f"qc.{gate}(q[{control}], q[{target}])\n"
        elif gate in ['rzz', 'rxx']:
            qubit1 = random.randint(0, num_qubits - 1)
            qubit2 = random.randint(0, num_qubits - 1)
            while qubit2 == qubit1:
                qubit2 = random.randint(0, num_qubits - 1)
            angle = random.uniform(0, 2*math.pi)
            code += f"qc.{gate}(math.pi/{int(2*math.pi/angle)}, q[{qubit1}], q[{qubit2}])\n"
        elif gate == 'ccx':
            control1 = random.randint(0, num_qubits - 1)
            control2 = random.randint(0, num_qubits - 1)
            target = random.randint(0, num_qubits - 1)
            while control2 == control1 or target == control1 or target == control2:
                control2 = random.randint(0, num_qubits - 1)
                target = random.randint(0, num_qubits - 1)
            code += f"qc.{gate}(q[{control1}], q[{control2}], q[{target}])\n"
        elif gate == 'cswap':
            control = random.randint(0, num_qubits - 1)
            target1 = random.randint(0, num_qubits - 1)
            target2 = random.randint(0, num_qubits - 1)
            while target1 == control or target2 == control or target1 == target2:
                target1 = random.randint(0, num_qubits - 1)
                target2 = random.randint(0, num_qubits - 1)
            code += f"qc.{gate}(q[{control}], q[{target1}], q[{target2}])\n"
    
    with open(filename, 'w') as f:
        f.write(code)

import os

# Define base and subdirectories using os.path.join for cross-platform compatibility
base_dir = "Testcases"
deep_dir = os.path.join(base_dir, "deep")
shallow_dir = os.path.join(base_dir, "shallow")

# Create directories if they do not already exist
os.makedirs(deep_dir, exist_ok=True)
os.makedirs(shallow_dir, exist_ok=True)

# Generate the random Qiskit circuits in the respective directories
for i in range(3):
    generate_random_qiskit_circuit(3, 25, os.path.join(deep_dir, f"deep_{i}.py"))       # depth = 25
    generate_random_qiskit_circuit(3, 5, os.path.join(shallow_dir, f"shallow_{i}.py"))    # depth = 5

import os
import subprocess

# Create the output directory for shallow entropies
entropies_shallow_dir = os.path.join("Entropies", "shallow")
os.makedirs(entropies_shallow_dir, exist_ok=True)

# Define other paths with os.path.join for cross-platform compatibility
testcases = os.path.join("Testcases", "shallow")
config = os.path.join("muskit", "executorConfig.py")
inputs = os.path.join("muskit", "testcases.py")
savePath = os.path.join("Entropies", "shallow", "shallow.txt")

process = subprocess.Popen(
    [
        "python",
        "-m", "muskit.ComandMain",
        "Execute",
        config,
        inputs,
        testcases,
        savePath
    ],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)
process.wait()

import os

# Construct file paths using os.path.join
shallow_path = os.path.join("Entropies", "shallow", "shallow.txt")
deep_path = os.path.join("Entropies", "deep", "deep.txt")

# Read shallow entropies
with open(shallow_path, 'r') as file:
    content = file.read().strip()
shallow_entropies = [float(x) for x in content.split(',') if x]

# Read deep entropies
with open(deep_path, 'r') as file:
    content = file.read().strip()
deep_entropies = [float(x) for x in content.split(',') if x]

print("Bugless shallow entropies: ", shallow_entropies)
print("Bugless deep entropies: ", deep_entropies)

import os
import subprocess

# Define the config file path.
config = os.path.join("muskit", "generatorConfig.py")

# Create the output directory for shallow mutants.
mutants_dir = os.path.join("Mutants", "shallow")
os.makedirs(mutants_dir, exist_ok=True)

# Define the testcases directory.
testcases_dir = os.path.join("Testcases", "shallow")

for file in os.listdir(testcases_dir):
    if file.endswith(".py"):
        name = os.path.splitext(file)[0]
        process = subprocess.Popen(
            [
                "python",
                "-m", "muskit.ComandMain",
                "Create",
                config,
                os.path.join(testcases_dir, file),
                os.path.join(mutants_dir, f"mutants_of_{name}")
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        process.wait()

