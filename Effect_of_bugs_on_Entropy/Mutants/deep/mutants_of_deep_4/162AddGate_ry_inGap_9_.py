import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.rzz(math.pi/1, q[2], q[0])
qc.ry(math.pi/1, q[0])
qc.rz(math.pi/1, q[1])
qc.s(q[0])
qc.t(q[0])
qc.swap(q[1], q[0])
qc.x(q[1])
qc.s(q[1])
qc.ry(3.141592653589793, q[0])
qc.rx(math.pi/1, q[0])
qc.swap(q[0], q[1])
qc.rz(math.pi/27, q[0])
qc.s(q[1])
qc.t(q[0])
qc.z(q[0])
qc.rzz(math.pi/5, q[1], q[0])
qc.y(q[2])
qc.p(math.pi/1, q[0])
qc.ry(math.pi/2, q[2])
qc.y(q[1])
qc.rz(math.pi/11, q[2])
qc.t(q[0])
qc.ccx(q[2], q[0], q[1])
qc.ry(math.pi/1, q[0])
qc.z(q[0])
qc.rzz(math.pi/1, q[2], q[0])
