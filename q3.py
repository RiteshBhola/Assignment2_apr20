"""
second order ode by RK4

let dy/dx=z=f(x,y,z)
    dz/dx=g(x,y,z)
"""
import numpy as np
import matplotlib.pyplot as plt
def solution(t):
 return (1/6)*(t**3)*np.exp(t) - t*np.exp(t)  + 2*np.exp(t) - t - 2

def scale(x):
	return(1-x)/(1+x)


def f(x,y,z):
	return(z)
	
def g(x,y,z):
	return(x*np.exp(x)-x-y+2*z)
	
h=0.01	
x=np.arange(0,1+h,h)	
n=x.size


y=np.zeros(n)
z=np.zeros(n)
y[0]=0
z[0]=0
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
	
	

plt.plot(x,solution(x),"-b",label="Analytic Solution")
plt.plot(x,y,"*r",label="RK4 Solution")
plt.xlabel("$x$",fontsize=20)
plt.ylabel("y(x)",fontsize=20)

plt.legend()
plt.show()
