import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.cz(q[2], q[0])
qc.rxx(1.5707963267948966,q[1], q[0])
qc.p(math.pi/2, q[2])
qc.ccx(q[1], q[0], q[2])
qc.rzz(math.pi/1, q[0], q[2])
