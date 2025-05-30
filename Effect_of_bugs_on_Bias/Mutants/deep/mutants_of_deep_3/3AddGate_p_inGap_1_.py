import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.p(3.141592653589793,q[0])
qc.y(q[0])
qc.z(q[2])
qc.t(q[2])
