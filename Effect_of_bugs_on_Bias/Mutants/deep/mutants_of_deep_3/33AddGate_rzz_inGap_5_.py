import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.y(q[0])
qc.z(q[2])
qc.t(q[2])

qc.rzz(3.141592653589793,q[2],q[1])