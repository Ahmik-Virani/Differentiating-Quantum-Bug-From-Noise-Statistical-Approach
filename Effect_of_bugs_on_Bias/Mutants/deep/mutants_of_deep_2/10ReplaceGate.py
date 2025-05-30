import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.rz(4.71238898038469,q[2])
qc.z(q[0])
qc.h(q[0])
