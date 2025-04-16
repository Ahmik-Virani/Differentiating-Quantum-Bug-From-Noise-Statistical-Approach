import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.ry(1.5707963267948966,q[2])
qc.z(q[0])
qc.h(q[0])
