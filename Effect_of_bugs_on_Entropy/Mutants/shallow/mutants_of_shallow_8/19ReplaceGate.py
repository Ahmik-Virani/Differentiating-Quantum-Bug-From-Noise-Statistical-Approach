import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.z(q[2])
qc.rx(1.5707963267948966,q[2])
qc.rx(math.pi/1, q[2])
qc.s(q[1])
qc.s(q[0])
