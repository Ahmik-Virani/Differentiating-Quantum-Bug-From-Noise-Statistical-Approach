import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.swap(q[2], q[1])
qc.cswap(q[2], q[0], q[1])
qc.h(q[0])

qc.rx(1.5707963267948966,q[1])