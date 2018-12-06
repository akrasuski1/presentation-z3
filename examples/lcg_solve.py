from z3 import *

gen = [ 74, 42, 34, 33, 34, 71, 0, 55, 56, 41, ]
state = BitVec("state", 32)
s = Solver()
for i in range(10):
    state = 1103515245 * state + 12345
    s.add(((state >> 16) & 0x7FFF) % 100 == gen[i])
print s.check()
print s.model()

