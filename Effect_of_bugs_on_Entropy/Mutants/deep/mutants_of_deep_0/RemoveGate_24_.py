import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.s(q[2])
qc.t(q[2])
qc.swap(q[1], q[2])
qc.cswap(q[0], q[1], q[2])
qc.h(q[1])
qc.rz(math.pi/3, q[2])
qc.s(q[2])
qc.z(q[1])
qc.y(q[2])
qc.t(q[1])
qc.cz(q[0], q[1])
qc.cswap(q[2], q[0], q[1])
qc.cx(q[2], q[0])
qc.ccx(q[1], q[0], q[2])
qc.rzz(math.pi/10, q[1], q[0])
qc.cswap(q[1], q[0], q[2])
qc.rz(math.pi/5, q[1])
qc.cx(q[1], q[0])
qc.swap(q[2], q[0])
qc.ccx(q[2], q[1], q[0])
qc.swap(q[2], q[0])
qc.cz(q[2], q[0])
qc.ry(math.pi/4, q[2])
qc.p(math.pi/2, q[0])
