"""
second order ode by RK4

let dy/dx=z=f(x,y,z)
    dz/dx=g(x,y,z)
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x,y,z):
	return(z)
	
def g(x,y,z):
	return(x*np.log(x)+2*(1/x)*z-2*y*(1/x**2))
	
def fun(x):
	return(7*x/4+(0.5*x**3)*np.log(x)-(3/4)*x**3)

h=0.001	
x=np.arange(1,2+h,h)	
n=x.size


y=np.zeros(n)
z=np.zeros(n)
y[0]=1
z[0]=0
for i in range(0,n-1,1):
	k0=h*f(x[i],y[i],z[i])
	l0=h*g(x[i],y[i],z[i])
	y[i+1]=y[i]+k0
	z[i+1]=z[i]+l0
	
	
plt.plot(x,y,"-b",label="Euler Method")
plt.plot(x,fun(x),"-.r",label="Analytic Solution")
plt.xlabel("$x$",fontsize=20)
plt.ylabel("y(x)",fontsize=20)
plt.legend()
plt.show()
