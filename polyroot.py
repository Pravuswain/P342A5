import math

#to create polynomials from coefficient5s
def polynomial(p):
	n = len(p)-1
	def f(x):
		g=0
		for i in range(0,n+1):
			g += p[i]*(x**(n-i))
		return g
	return f
#function for derivative
def derivative(f,h = 10**-6):
    def Df(x):
        return (f(x+h)-f(x-h))/(2*h)
    return Df

def laguerremethod(f,p,a,E):
#empty array
	X = []
	#order of polynomial
	n = len(p)-1
	#define the derivatives
	while n >0 :
		Df = derivative(f)
		D2f = derivative(Df)
		#if the chosen point is solution
		if f(a) == 0:
			X.append(a)
			p = deflation(p,a,n)
			f = polynomial(p)
			n -= 1
		#setting a value 	
		else:
			G =0
			H = 0
			b = 1

			while b >E:
				G =Df(a)/f(a)
				H =(G*G) -(D2f(a)/f(a))
				if G<0:
					j= -1
				else:
					j =1
				b = n/(G + j*(math.sqrt((n-1)*((n*H)-(G*G)))))
				a -= b

		
			X.append(a)
			p = deflation(p,a,n)
			f = polynomial(p)
			n -= 1				


	return X			
def deflation(p,a,n):
	y=[]
	y.append(p[0])
	for i in range(1,n):
		b=p[i]+a*y[-1]
		y.append(b)
	return y

	








