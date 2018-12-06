from z3 import *
x1 = Bool('x1')
x2 = Bool('x2')
solve(Or(x1, x2) == And(x1, x2))
