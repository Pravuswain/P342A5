
from polyroot import polynomial

from polyroot import laguerremethod

P = [1,-3,-7,27,-18]
f = polynomial(P)


out = laguerremethod(f,P,4,10**(-6))

print(f'roots of polynomial = {out}')

#OUTPUT
'''
roots of polynomial = [2.9999999999999982, 2.0000000000000044, 1.0000000000000286, -3.000000000000031]
'''


