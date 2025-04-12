import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.cz(q[2], q[0])
qc.swap(q[1], q[0])
qc.id( q[2])
qc.ccx(q[1], q[0], q[2])
qc.rzz(math.pi/1, q[0], q[2])
