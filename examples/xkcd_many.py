from z3 import *

a, b, c, d, e, f = Ints('a b c d e f')
s = Solver()
s.add(215*a + 275*b + 335*c + 355*d + 420*e + 580*f == 1505, 
    a>=0, b>=0, c>=0, d>=0, e>=0, f>=0,
    a<=10, b<=10, c<=10, d<=10, e<=10, f<=10)

while s.check() == sat:
    m = s.model()
    print m
    s.add(Or([
        var() != m[var] 
        for var in m]))
