import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.p(1.5707963267948966, q[1])
qc.ry(math.pi/1, q[1])
qc.rz(math.pi/1, q[0])
qc.sx(q[0])
