import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.cswap(q[1], q[0], q[2])
qc.swap(q[0], q[1])
qc.rzz(3.141592653589793,q[1], q[2])
qc.cz(q[2], q[0])
qc.rzz(math.pi/4, q[2], q[1])
