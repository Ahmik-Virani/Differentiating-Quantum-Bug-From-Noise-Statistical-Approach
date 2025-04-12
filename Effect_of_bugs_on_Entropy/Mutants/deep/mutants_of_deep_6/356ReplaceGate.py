import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.cswap(q[1], q[0], q[2])
qc.cz(q[0], q[1])
qc.ccx(q[1], q[2], q[0])
qc.x(q[2])
qc.ccx(q[0], q[2], q[1])
qc.cswap(q[2], q[0], q[1])
qc.swap(q[2], q[1])
qc.ccx(q[1], q[0], q[2])
qc.ccx(q[0], q[2], q[1])
qc.rzz(math.pi/8, q[0], q[2])
qc.cswap(q[2], q[0], q[1])
qc.cswap(q[2], q[0], q[1])
qc.z(q[2])
qc.s(q[1])
qc.s(q[1])
qc.id(q[2])
qc.h(q[0])
qc.ry(math.pi/13, q[2])
qc.rxx(math.pi/1, q[0], q[2])
qc.rxx(math.pi/2, q[0], q[2])
qc.p(math.pi/3, q[2])
qc.rx(3.141592653589793,q[0])
qc.sx(q[1])
qc.rzz(math.pi/1, q[0], q[2])
qc.rx(math.pi/26, q[1])
