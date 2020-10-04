import math
import csv

def derivative(f,h = 10**-6):
    def Df(x):
        return (f(x+h)-f(x-h))/(2*h)
    return Df


def bisection(f,a,b,N,E,name):
#check for good intervals
	if f(a)*f(b)>=0:
		print(f'try new interval')
		return None
#for convinience in looping use n as subcript		
	a_n = a
	b_n = b
	print(f'Bisection method :')
	
	for n in range(1,N+1):
		#setting c (midpoint of interval)
		c_n = (a_n + b_n)/2
		
		
		y=abs(b_n-a_n)
		#use conditions to determine position of c and a or b shifting accordingly with each iteration
		if f(a_n)*f(c_n)<0:
			a_n=a_n
			b_n=c_n

		elif f(a_n)*f(c_n)>0:
			a_n=c_n
			b_n=b_n
		#absolute error
		elif  abs(b_n-a_n) < E :
			return c_n
		else:
			print(f'fail')
			return None
		with open(name,'a') as data:
			print(n,',',y,file =data)
	print(f'root = {(a_n + b_n)/2}')		
	return N

def regulafalsi(f,a,b,N,E,name):
#check for good intervals
	if f(a)*f(b)>=0:
		print(f'try new interval')
		return None
#for convinience in looping use n as subcript		
	a_n = a
	b_n = b
	print(f'False Position method :')

	for n in range(1,N+1):
		m=n-1

		#setting c (midpoint of interval)
		c_n = b_n - (((b_n-a_n)*f(b_n))/(f(b_n)-f(a_n)))
		y=  abs(b_n- a_n)
		#use condiions for shifting a or b with each iteration
		if f(a_n)*f(c_n)<0:
			a_n=a_n
			b_n=c_n

		elif f(a_n)*f(c_n)>0:
			a_n=c_n
			b_n=b_n
		#absolute error
		elif abs(b_n-a_n) < E :
			return c_n
		else:
			print(f'fail')
			return None
		with open(name,'a') as data:
			print(n,',',y,file =data)	
	print(f'root = {c_n}')
	return N
		

def newtonraph(f,x,N,E,name):
#set the x_n as X_0 to begin the operation
	x_n = x
	#loop to increase subscript 
	for n in range(1,N+1):
		#use condition to reach the precision
		if abs(f(x_n))	< E:

			return x_n
		Df= derivative(f)
		#replace the x_n with approx roots
		b = (f(x_n)/Df(x_n))
		x_n = x_n - b
		with open(name,'a') as data:
			print(n,',',b,file =data)

		if derivative(x_n) == 0:
			return None
	return None

