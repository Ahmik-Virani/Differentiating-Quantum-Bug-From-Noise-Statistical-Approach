import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.s(q[0])
qc.s(q[0])
qc.cswap(q[0], q[2], q[1])
qc.y(q[2])
qc.y(q[1])
qc.z(q[2])
qc.y(q[0])
qc.y(q[2])
qc.t(q[0])
qc.rx(4.71238898038469,q[2])
qc.t(q[2])
qc.rzz(math.pi/14, q[1], q[0])
qc.cx(q[1], q[0])
qc.cswap(q[2], q[0], q[1])
qc.rzz(math.pi/4, q[0], q[2])
qc.h(q[1])
qc.cz(q[1], q[0])
qc.rz(math.pi/2, q[1])
qc.y(q[1])
qc.h(q[1])
qc.id(q[2])
qc.cz(q[1], q[2])
qc.rz(math.pi/5, q[1])
qc.p(math.pi/1, q[1])
qc.rzz(math.pi/2, q[0], q[1])
qc.t(q[2])
