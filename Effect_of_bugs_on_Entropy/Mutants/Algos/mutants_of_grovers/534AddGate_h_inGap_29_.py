import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.ry(math.pi/2, q[0])
qc.ry(math.pi/-2, q[1])
qc.rz(math.pi/-3, q[2])
qc.ry(math.pi/2, q[2])
qc.cx(q[1], q[2])
qc.ry(math.pi/1, q[1])
qc.rx(math.pi/-1, q[2])
qc.rz(math.pi/-3, q[2])
qc.cx(q[0], q[2])
qc.p(math.pi/4, q[2])
qc.cx(q[1], q[2])
qc.p(math.pi/4, q[1])
qc.p(math.pi/-3, q[2])
qc.cx(q[0], q[2])
qc.cx(q[0], q[1])
qc.p(math.pi/4, q[0])
qc.p(math.pi/-3, q[1])
qc.cx(q[0], q[1])
qc.rx(math.pi/1, q[0])
qc.p(math.pi/4, q[2])
qc.cx(q[1], q[2])
qc.p(math.pi/-3, q[2])
qc.cx(q[0], q[2])
qc.rx(math.pi/1, q[0])
qc.p(math.pi/4, q[2])
qc.cx(q[1], q[2])
qc.rz(math.pi/-4, q[1])
qc.rx(math.pi/1, q[1])
qc.h( q[2])
qc.rz(math.pi/1, q[2])
qc.rx(math.pi/1, q[2])
qc.cx(q[0], q[2])
qc.cx(q[0], q[1])
qc.ry(math.pi/1, q[0])
qc.rz(math.pi/-1, q[1])
qc.ry(math.pi/1, q[1])
qc.rz(math.pi/1, q[1])
qc.cx(q[0], q[1])
qc.rz(math.pi/4, q[0])
qc.ry(math.pi/2, q[0])
qc.rz(math.pi/-1, q[1])
qc.ry(math.pi/1, q[1])
qc.rz(math.pi/-1, q[2])
qc.ry(math.pi/3, q[2])
qc.rz(math.pi/-1, q[2])
qc.cx(q[1], q[2])
qc.p(math.pi/-3, q[2])
qc.cx(q[0], q[2])
qc.p(math.pi/4, q[2])
qc.cx(q[1], q[2])
qc.rz(math.pi/1, q[1])
qc.rx(math.pi/-3, q[1])
qc.p(math.pi/-3, q[2])
qc.cx(q[0], q[2])
qc.rz(math.pi/1, q[0])
qc.cx(q[0], q[1])
qc.ry(math.pi/1, q[0])
qc.rz(math.pi/-1, q[1])
qc.ry(math.pi/1, q[1])
qc.rz(math.pi/1, q[1])
qc.cx(q[0], q[1])
qc.rz(math.pi/1, q[0])
qc.ry(math.pi/2, q[0])
qc.rz(math.pi/-1, q[1])
qc.ry(math.pi/-3, q[1])
qc.rz(math.pi/-1, q[2])
qc.ry(math.pi/-2, q[2])
