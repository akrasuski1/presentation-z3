from z3 import *

x0, y0 = BitVecs('x y', 32)

x, y = x0, y0
x = x ^ y
y = x ^ y
x = x ^ y

s = Solver()
s.add(Or(x != y0, y != x0))
print s.check()
