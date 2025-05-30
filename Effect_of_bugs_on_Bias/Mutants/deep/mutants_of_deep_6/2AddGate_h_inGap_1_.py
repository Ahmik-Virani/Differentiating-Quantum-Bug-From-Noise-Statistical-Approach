import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.h(q[1])
qc.t(q[1])
qc.h(q[2])
qc.rz(math.pi/1, q[1])
