import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.y(q[2])
qc.z(q[2])
qc.x(q[2])
qc.rx(math.pi/1, q[2])
qc.s(q[1])
qc.s(q[0])
