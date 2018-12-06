from z3 import *

opt = Optimize()
x, y, f = Ints('x y f')
opt.minimize((x-1)*(x-1) + y*y)
print opt.check()
print opt.model()
