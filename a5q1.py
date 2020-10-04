import math


print('For function 1:')
from nonlinearoot import bisection

f = lambda x : math.log(x) - math.sin(x)

out1 = bisection(f,1.5,2.5,25,10**(-4),'bisectq1.txt')

print(out1)

from nonlinearoot import regulafalsi


out2 = regulafalsi(f,1.5,2.5,15,10**(-6),'falseq1.txt')

print(out2)

from nonlinearoot import newtonraph

out3 = newtonraph(f,1.5,10,10**(-6),'newtonq1.txt' )
print('Newton-Raphson method :')
print(f'root = {out3}')


print('\nfor function 2')

from nonlinearoot import bisection

f = lambda x :-x - math.cos(x)

out1 = bisection(f,-1.5,2.5,25,10**(-4),'bisectq1b.txt')

print(out1)

from nonlinearoot import regulafalsi


out2 = regulafalsi(f,-1.5,2.5,15,10**(-6),'falseq1b.txt')

print(out2)

from nonlinearoot import newtonraph

out3 = newtonraph(f,0,10,10**(-6),'newtonq1b.txt' )
print('Newton-Raphson method :')
print(f'root = {out3}')

#OUTPUT
'''
For function 1:
Bisection method :
root = 2.219107136130333
25
False Position method :
root = 2.219107148913746
15
Newton-Raphson method :
root = 2.2191071502170927

for function 2
Bisection method :
root = -0.7390851229429245
25
False Position method :
root = -0.7390851332149052
15
Newton-Raphson method :
root = -0.7390851333852848

'''