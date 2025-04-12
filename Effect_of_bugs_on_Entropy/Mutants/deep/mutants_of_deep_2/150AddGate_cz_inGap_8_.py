import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.rzz(math.pi/3, q[1], q[0])
qc.ccx(q[1], q[2], q[0])
qc.cswap(q[0], q[2], q[1])
qc.h(q[2])
qc.ry(math.pi/2, q[0])
qc.s(q[0])
qc.swap(q[0], q[2])
qc.cz(q[2], q[1])
qc.cx(q[2], q[1])
qc.p(math.pi/1, q[2])
qc.cswap(q[2], q[1], q[0])
qc.ccx(q[2], q[0], q[1])
qc.t(q[1])
qc.rxx(math.pi/20, q[0], q[1])
qc.id(q[0])
qc.ccx(q[2], q[0], q[1])
qc.cz(q[0], q[1])
qc.rxx(math.pi/8, q[0], q[1])
qc.rxx(math.pi/2, q[1], q[0])
qc.cswap(q[0], q[1], q[2])
qc.cx(q[0], q[1])
qc.rx(math.pi/1, q[2])
qc.y(q[0])
qc.t(q[0])
qc.ccx(q[2], q[1], q[0])
qc.rz(math.pi/1, q[1])
