import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.rzz(math.pi/5, q[0], q[1])
qc.y(q[2])
qc.id(q[0])

qc.swap(q[2],q[1])