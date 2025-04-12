import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.z(q[0])
qc.rz(math.pi/1, q[2])
qc.rz(math.pi/2, q[0])
qc.h(q[2])
qc.z(q[0])
qc.z(q[1])
qc.rzz(math.pi/1, q[2], q[1])
qc.x(q[2])
qc.x(q[1])
qc.id(q[0])
qc.h(q[1])
qc.ry(math.pi/3, q[0])
qc.s(q[1])
qc.rxx(math.pi/1, q[0], q[2])
qc.rxx(math.pi/1, q[2], q[1])
qc.s(q[0])
qc.y(q[2])
qc.p(math.pi/2, q[0])
qc.y(q[0])
qc.p(math.pi/1100, q[1])
qc.x(q[1])
qc.swap(q[2], q[0])
qc.rxx(math.pi/3, q[1], q[2])
qc.s(q[0])
qc.z(q[2])

qc.sx(q[0])