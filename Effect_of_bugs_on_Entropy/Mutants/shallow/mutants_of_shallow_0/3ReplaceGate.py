import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.p(3.141592653589793,q[0])
qc.ccx(q[2], q[1], q[0])
qc.cswap(q[2], q[0], q[1])
qc.y(q[2])
qc.s(q[2])
