from z3 import *

v, p = BitVecs('v p', 32)

s = Solver()
s.add(Not(Implies(
    (v & (v - 1)) == 0,
    Exists(p, And(p>=0, p<32, (BitVecVal(1, 32) << p) == v))
)))
print s.check()
print s.model()
