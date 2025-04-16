import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.rz(1.5707963267948966, q[1])
qc.ccx(q[0], q[2], q[1])
qc.cz(q[0], q[2])
qc.ccx(q[2], q[0], q[1])
