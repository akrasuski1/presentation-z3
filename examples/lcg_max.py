from z3 import *
import time

state = BitVec("state", 32)
initial = state
s = Solver()
t = time.time()
s.add(state > t, state < t + 60*60*24)
for i in range(4):
    state = 1103515245 * state + 12345
    s.add(((state >> 16) & 0x7FFF) % 10 == 9)
print s.check()
m = s.model()
print "Wait", m[initial].as_long() - t, "seconds"
