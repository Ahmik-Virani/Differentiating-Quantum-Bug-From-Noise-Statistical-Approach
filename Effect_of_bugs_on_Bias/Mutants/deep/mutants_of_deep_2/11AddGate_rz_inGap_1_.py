import math
from qiskit import *

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')
qc = QuantumCircuit(q, c)

qc.rz(3.141592653589793, q[2])
qc.rxx(math.pi/3, q[1], q[2])
qc.z(q[1])
qc.id(q[1])
