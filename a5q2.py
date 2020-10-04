
from polyroot import polynomial

from polyroot import laguerremethod

P = [1,-3,-7,27,-18]
f = polynomial(P)


out = laguerremethod(f,P,4,10**(-6))

print(f'roots of polynomial = {out}')


