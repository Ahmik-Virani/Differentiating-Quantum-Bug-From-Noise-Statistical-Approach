import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.y( q[0])
qc.ccx(q[2], q[1], q[0])
qc.cswap(q[2], q[1], q[0])
qc.x(q[0])
