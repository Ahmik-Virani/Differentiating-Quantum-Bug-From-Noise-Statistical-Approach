import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.rxx(math.pi/1, q[0], q[2])
qc.y(q[0])
qc.ccx(q[2], q[0], q[1])
qc.s(q[0])
qc.swap(q[2], q[0])
qc.t(q[1])
qc.swap(q[2], q[1])
qc.y(q[0])
qc.h(q[2])
qc.rx(math.pi/73, q[2])
qc.p(math.pi/2, q[0])
qc.sx(q[2])
qc.rzz(math.pi/11, q[1], q[0])
qc.rzz(math.pi/1, q[1], q[2])
qc.swap(q[2], q[1])
qc.cx(q[2], q[0])
qc.sx(q[1])
qc.p(math.pi/344, q[0])
qc.h(q[1])
qc.swap(q[2], q[0])
qc.id(q[2])
qc.t(q[0])
qc.t(q[0])
qc.swap(q[0], q[1])
qc.y(q[2])
qc.cswap(q[1], q[0], q[2])