import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.rz(1.5707963267948966, q[0])
qc.ccx(q[1], q[2], q[0])
qc.x(q[1])
qc.ry(math.pi/2, q[1])
