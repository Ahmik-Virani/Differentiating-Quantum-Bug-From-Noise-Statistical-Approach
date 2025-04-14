import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.h( q[2])
qc.rxx(math.pi/3, q[1], q[2])
qc.z(q[1])
qc.id(q[1])
