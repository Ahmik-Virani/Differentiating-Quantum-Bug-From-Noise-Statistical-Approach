import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.ccx(q[1], q[0], q[2])
qc.y(q[2])
qc.z(q[0])
qc.h(q[0])
