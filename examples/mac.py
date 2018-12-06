from z3 import *
shake = Real("shake")
ham = Real("hamburger")
fries = Real("fries")
res = Real("result")
solve(shake + shake + shake == 30,
        shake + ham + ham == 20,
        ham + 2*fries + 2*fries == 9,
        ham + fries * shake == res)
