# Effect of bugs on Entropy

This directory contains the experiments to study the effects of bugs on the entropy of a quantum circuit. To do this, the following steps are done:
* random quantum circuits are generated, some deep with a depth of 25 and some shallow with a depth of 5. 
* Mutants of these circuits are created and the entropies of the outputs of these mutants are calculated. 
* These entropies are then used to estimate probability density curves, in which we check how the entropies of the mutants differ from the entropy of the original circuit.

This directory has the following contents:

* **_create\_distributions.ipynb_**: Contains code to generate the testcases(random quantum circuits and some algorithms), create their mutants, and store the entropies and the distribution of entropies of these mutants.
*  **_Algos_**: Contains the quantum circuit of Grover's Algorithm.
* **_Distributions_**: Contains the Probability density curves for the entropies of the mutants of each testcase.
* **_Entropies_**: Contains the entropies of the mutants of each testcase.
* **_muskit_**: Contains the source code of [ **`muskit`**](https://github.com/Simula-COMPLEX/muskit).
* **_Mutants_**: Contains the mutants of each testcase.
* **_Testcases_**: Contains the randomly generated testcases.

All tests are done on circuits with 3 qubits. The number of qubits for testing can be changed in **_create\_distributions.ipynb_**.

The randomly generated testcases are divided into two categories:
* **deep**: having a depth of 25.
* **shallow**: having a depth of 5.

The depths can be changed in **_create\_distributions.ipynb_**.