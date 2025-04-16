import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.rzz(math.pi/5, q[1], q[2])
qc.y(q[2])
qc.cz(q[2], q[1])

qc.rz(3.141592653589793,q[1])