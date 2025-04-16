import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.swap(q[2], q[1])
qc.cswap(q[2], q[0], q[1])
qc.ry(3.141592653589793,q[0])
