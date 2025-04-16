import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.ccx(q[2], q[1], q[0])
qc.cswap(q[2], q[1], q[0])
qc.rz(4.71238898038469,q[0])
