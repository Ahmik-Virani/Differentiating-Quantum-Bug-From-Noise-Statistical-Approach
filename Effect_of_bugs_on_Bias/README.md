
## Overview
This series of experiments automates the generation of random Qiskit circuits, creates mutants of those circuits, executes each mutant to measure output biases, and computes summary statistics (sum, count, average) of those biases. It’s designed to help you explore how small changes (“mutants”) affect the statistical behavior of quantum circuits.

## Features
- **Random Circuit Generation**  
  Generate parameterized random circuits with any number of qubits and operations.
- **Mutant Creation**  
  Leverage a separate `muskit` module to apply controlled mutations to each circuit.
- **Automated Execution**  
  Run every mutant through a test harness to capture bias data.
- **Bias Analysis**  
  Parse the resulting comma‑separated bias files, compute totals, counts, and averages.

## Prerequisites
- Python 3.8+  
- Qiskit  
- `tqdm` for progress bars  
- `numpy`, `scipy`, and `matplotlib` (optional, for further statistical analysis or plotting)  
- A local `muskit` package containing:  
  - `generatorConfig.py`  
  - `executorConfig.py`  
  - `testcases.py`  

Install dependencies with:
```bash
pip install qiskit tqdm numpy scipy matplotlib
```

## Usage

1. **Generate Random Circuits**  
   - Cleans & recreates `Testcases/deep` and `Testcases/shallow`  
   - Produces N circuits per folder (default: 3)

2. **Create Mutants**  
   - Reads each `.py` in `Testcases/deep`  
   - Invokes `muskit.ComandMain Create` to output into `Mutants/deep`

3. **Execute Mutants & Collect Bias**  
   - Iterates over every mutant folder in `Mutants/deep`  
   - Runs `muskit.ComandMain Execute` to produce a `.txt` of comma‑separated biases in `Bias/deep`

4. **Analyze Bias Files**  
   - For each `*.txt` in `Bias/deep`, prints:  
     ```
     <mutant_name>: sum = <total>, count = <n>, avg = <average>
     ```

## Configuration
- **`muskit/generatorConfig.py`**  
  Defines mutation rules and operators.  
- **`muskit/executorConfig.py`**  
  Specifies how to execute circuits and collect measurement data.  

