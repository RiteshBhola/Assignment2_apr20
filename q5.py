import numpy as np
import matplotlib.pyplot as plt

def f(x,y,z):
	return(z)
	
def g(x,y,z):
	return(-10)
	
h=0.1	
x=np.arange(0,10+h,h)	
n=x.size


y=np.zeros(n)
z=np.zeros(n)
y[0]=0
"Initial guess t"
t1=10
t2=20
z1=0
z2=0
#Obtaining the solution at two initial guesses t1 and t2 then following secant method for increment the guess
z[0]=t1

for i in range(0,n-1,1):
	k0=h*f(x[i],y[i],z[i])
	l0=h*g(x[i],y[i],z[i])
	k1=h*f(x[i]+h/2,y[i]+k0/2,z[i]+l0/2)
	l1=h*g(x[i]+h/2,y[i]+k0/2,z[i]+l0/2)
	k2=h*f(x[i]+h/2,y[i]+k1/2,z[i]+l1/2)
	l2=h*g(x[i]+h/2,y[i]+k1/2,z[i]+l1/2)
	k3=h*f(x[i]+h,y[i]+k2,z[i]+l2)
	l3=h*g(x[i]+h,y[i]+k2,z[i]+l2)
	y[i+1]=y[i]+(k0+2*k1+2*k2+k3)/6
	z[i+1]=z[i]+(l0+2*l1+2*l2+l3)/6

z1=y[n-1]
plt.plot(x,y)
z[0]=t2

for i in range(0,n-1,1):
	k0=h*f(x[i],y[i],z[i])
	l0=h*g(x[i],y[i],z[i])
	k1=h*f(x[i]+h/2,y[i]+k0/2,z[i]+l0/2)
	l1=h*g(x[i]+h/2,y[i]+k0/2,z[i]+l0/2)
	k2=h*f(x[i]+h/2,y[i]+k1/2,z[i]+l1/2)
	l2=h*g(x[i]+h/2,y[i]+k1/2,z[i]+l1/2)
	k3=h*f(x[i]+h,y[i]+k2,z[i]+l2)
	l3=h*g(x[i]+h,y[i]+k2,z[i]+l2)
	y[i+1]=y[i]+(k0+2*k1+2*k2+k3)/6
	z[i+1]=z[i]+(l0+2*l1+2*l2+l3)/6
	
z2=y[n-1]	
	
t3=t2-((y[n-1]-0)*(t2-t1))/(z2-z1)
z[0]=t3

coun=0
for m in range(0,50,1):	
	plt.plot(x,y,label="canditate solution")
	++coun
	for i in range(0,n-1,1):
		k0=h*f(x[i],y[i],z[i])
		l0=h*g(x[i],y[i],z[i])
		k1=h*f(x[i]+h/2,y[i]+k0/2,z[i]+l0/2)
		l1=h*g(x[i]+h/2,y[i]+k0/2,z[i]+l0/2)
		k2=h*f(x[i]+h/2,y[i]+k1/2,z[i]+l1/2)
		l2=h*g(x[i]+h/2,y[i]+k1/2,z[i]+l1/2)
		k3=h*f(x[i]+h,y[i]+k2,z[i]+l2)
		l3=h*g(x[i]+h,y[i]+k2,z[i]+l2)
		y[i+1]=y[i]+(k0+2*k1+2*k2+k3)/6
		z[i+1]=z[i]+(l0+2*l1+2*l2+l3)/6	
	t1=t2
	t2=t3
	print(t1,t2)
	z1=z2
	z2=y[n-1]
	t3=t2-((y[n-1]-0)*(t2-t1))/(z2-z1)
	z[0]=t3
	if(np.abs(t2-t1)<0.000001):
		break
plt.plot(x,y,label="Final Solution")
#forming more canditates
t1=55
for k in range(0,3,1):
	z[0]=t1

	for i in range(0,n-1,1):
		k0=h*f(x[i],y[i],z[i])
		l0=h*g(x[i],y[i],z[i])
		k1=h*f(x[i]+h/2,y[i]+k0/2,z[i]+l0/2)
		l1=h*g(x[i]+h/2,y[i]+k0/2,z[i]+l0/2)
		k2=h*f(x[i]+h/2,y[i]+k1/2,z[i]+l1/2)
		l2=h*g(x[i]+h/2,y[i]+k1/2,z[i]+l1/2)
		k3=h*f(x[i]+h,y[i]+k2,z[i]+l2)
		l3=h*g(x[i]+h,y[i]+k2,z[i]+l2)
		y[i+1]=y[i]+(k0+2*k1+2*k2+k3)/6
		z[i+1]=z[i]+(l0+2*l1+2*l2+l3)/6

	z1=y[n-1]
	plt.plot(x,y,label="canditate solution")
	t1+=25


plt.legend()
plt.xlabel("$x$",fontsize=20)
plt.ylabel("y(x)",fontsize=20)
plt.show()
