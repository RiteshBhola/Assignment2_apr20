import numpy as np
import matplotlib.pyplot as plt

def f(x,y,z):
	return(-10)

def fy(x,y,z):
	return(0)
	
def fyprime(x,y,z):
	return(0)
	
N=100
a=0
b=10
h=(b-a)/(N+1)

y=np.zeros(N+2)
xx=np.arange(a,b+h,h)

A=np.zeros(N+2)
B=np.zeros(N+2)
C=np.zeros(N+2)
D=np.zeros(N+2)
l=np.zeros(N+2)
u=np.zeros(N+2)
z=np.zeros(N+2)
v=np.zeros(N+2)
y[0]=0
y[N+1]=0
for i in range(0,N+2,1):
			xx[i]=a+i*h
for i in range(1,N+1,1):
	y[i]=y[0] + i*(y[N+1]-y[0])/(b-a)


k=1
MAX=200
while(k<MAX):
	x=a+h
	plt.plot(xx,y,label="canditate solution")	
	t=(y[2]-y[0])/(2*h)
	A[1]=2+ h*h*fy(x,y[1],t)
	B[1]=-1+ 0.5*h*fyprime(x,y[1],t)
	D[1]=-(2*y[1]-y[2]-y[0]+h*h*f(x,y[1],t))
	
	for i in range(2,N):
		x=a+i*h
		t=(y[i+1]-y[i-1])/(2*h)
		A[i]=2+ h*h*fy(x,y[i],t)
		B[i]=-1+ 0.5*h*fyprime(x,y[i],t)
		C[i]=-1- 0.5*h*fyprime(x,y[i],t)
		D[i]=-(2*y[i]-y[i+1]-y[i-1]+h*h*f(x,y[i],t))

	x=b-h
	t=(y[N+1]-y[N-1])/(2*h)
	A[N]=2+ h*h*fy(x,y[N],t)
	B[N]=-1+ 0.5*h*fyprime(x,y[N],t)
	C[N]=-1- 0.5*h*fyprime(x,y[N],t)
	D[N]=-(2*y[N]-y[N-1]-y[N+1]+h*h*f(x,y[N],t))

	l[1]=A[1]
	u[1]=B[1]/A[1]
	z[1]=D[1]/l[1]
	
	for i in range(2,N):
		l[i]=A[i]-C[i]*u[i-1]
		u[i]=B[i]/l[i]
		z[i]=(D[i]-C[i]*z[i-1])/l[i]
		
	l[N]=A[N]-C[N]*u[N-1]
	z[N]=(D[N]-C[N]*z[N-1])/l[N]
	
	v[N]=z[N]
	y[N]=y[N]+v[N]
	
	for i in range(N-1,0,-1):
		v[i]=z[i]-u[i]*v[i+1]
		y[i]=y[i]+v[i]
	print(v)	
	if(np.sqrt((np.dot(v,v)))<10**(-3)):
		for i in range(0,N+2,1):
			xx[i]=a+i*h
		break
	
	k=k+1

plt.plot(xx,y,label="final solution")
#making canditates
def can(x):
	return(-(x-10)*x)


plt.xlabel("$x$",fontsize=20)
plt.ylabel("y(x)",fontsize=20)
plt.plot(xx,can(xx),label="candiate solution")
plt.plot(xx,3*can(xx),label="candiate solution")
plt.plot(xx,7*can(xx),label="candiate solution")
plt.legend()
plt.show()
