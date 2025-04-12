import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.ccx(q[2], q[0], q[1])
qc.rx(math.pi/1, q[0])
qc.y(q[1])
qc.rxx(math.pi/21, q[1], q[0])
qc.s(q[1])
qc.cx(q[2], q[1])
qc.id(q[0])
qc.s(q[2])
qc.cx(q[0], q[2])
qc.rzz(math.pi/2, q[1], q[0])
qc.cx(q[0], q[1])
qc.rx(3.141592653589793,q[0])
qc.x(q[0])
qc.rz(math.pi/10, q[1])
qc.cx(q[1], q[2])
qc.y(q[0])
qc.sx(q[1])
qc.sx(q[2])
qc.cswap(q[2], q[0], q[1])
qc.sx(q[1])
qc.rxx(math.pi/1, q[1], q[0])
qc.y(q[0])
qc.y(q[0])
qc.z(q[2])
qc.sx(q[2])
qc.y(q[1])
