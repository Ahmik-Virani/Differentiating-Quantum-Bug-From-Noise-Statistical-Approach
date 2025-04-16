import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.y(q[2])
qc.z(q[0])
qc.h(q[0])
qc.cswap(q[2], q[0], q[1])