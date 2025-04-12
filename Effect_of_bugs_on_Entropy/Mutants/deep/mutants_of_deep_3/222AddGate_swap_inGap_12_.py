import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.x(q[0])
qc.id(q[1])
qc.ccx(q[2], q[1], q[0])
qc.id(q[2])
qc.cx(q[0], q[1])
qc.rxx(math.pi/2, q[1], q[2])
qc.sx(q[2])
qc.z(q[2])
qc.p(math.pi/1, q[0])
qc.rx(math.pi/2, q[2])
qc.cx(q[2], q[0])
qc.swap(q[2],  q[1])
qc.cswap(q[2], q[0], q[1])
qc.h(q[0])
qc.ry(math.pi/1, q[1])
qc.rxx(math.pi/49, q[2], q[0])
qc.cx(q[0], q[1])
qc.h(q[0])
qc.id(q[1])
qc.y(q[2])
qc.x(q[2])
qc.ccx(q[0], q[2], q[1])
qc.cz(q[0], q[1])
qc.ccx(q[0], q[1], q[2])
qc.rxx(math.pi/1, q[0], q[1])
qc.cx(q[0], q[1])
