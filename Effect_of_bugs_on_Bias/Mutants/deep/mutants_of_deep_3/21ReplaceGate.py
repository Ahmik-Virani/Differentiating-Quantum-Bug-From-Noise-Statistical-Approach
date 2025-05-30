import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.y(q[0])
qc.z(q[2])
qc.rz(4.71238898038469,q[2])
