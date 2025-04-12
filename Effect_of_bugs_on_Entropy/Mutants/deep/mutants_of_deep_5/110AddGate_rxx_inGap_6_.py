import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.cz(q[2], q[0])
qc.sx(q[1])
qc.t(q[0])
qc.ry(math.pi/2, q[0])
qc.cx(q[2], q[1])
qc.rxx(0.0, q[0], q[2])
qc.rxx(math.pi/1, q[0], q[2])
qc.t(q[0])
qc.id(q[1])
qc.sx(q[2])
qc.y(q[1])
qc.cx(q[0], q[1])
qc.ry(math.pi/1, q[2])
qc.ccx(q[0], q[1], q[2])
qc.cx(q[1], q[0])
qc.p(math.pi/1, q[2])
qc.ccx(q[0], q[2], q[1])
qc.swap(q[1], q[2])
qc.z(q[0])
qc.rxx(math.pi/3, q[0], q[2])
qc.x(q[1])
qc.rzz(math.pi/1, q[1], q[0])
qc.rxx(math.pi/2, q[1], q[0])
qc.ry(math.pi/1, q[0])
qc.rx(math.pi/1, q[2])
qc.ccx(q[0], q[1], q[2])
