import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.rxx(math.pi/1, q[1], q[0])
qc.sx(q[2])
qc.z(q[0])
qc.t(q[1])
