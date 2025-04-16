import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.cswap(q[1], q[2], q[0])
qc.y(q[0])
qc.z(q[2])
qc.t(q[2])
