import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.cz(q[1], q[2])
qc.y(q[2])
qc.rzz(4.71238898038469,q[0], q[2])
qc.cz(q[1], q[2])
qc.x(q[2])
