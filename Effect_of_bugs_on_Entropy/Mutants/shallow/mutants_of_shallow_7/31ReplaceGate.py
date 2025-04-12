import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.cz(q[0], q[2])
qc.t(q[2])
qc.cx(q[2], q[0])
qc.rx(math.pi/6, q[2])
qc.swap( q[1], q[0])
