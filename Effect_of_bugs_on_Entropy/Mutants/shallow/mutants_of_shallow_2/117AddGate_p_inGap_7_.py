import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.ry(math.pi/2, q[0])
qc.rx(math.pi/31, q[1])
qc.y(q[2])
qc.id(q[0])
qc.rz(math.pi/2, q[2])

qc.p(4.71238898038469,q[1])