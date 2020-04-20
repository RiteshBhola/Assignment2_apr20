import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

"""
Tranformation is used t=(z-1)/(z+1)
and f(t,x) is also changed to f(z,x)
z,t is independent variable
x is dependent variable
"""

def f(x,y):
	a=(y**2)*((1-x)**2) + (1+x)**2
	return(2/a)
	

	
h=0.01	
x=np.arange(-1,1+h,h)	
n=x.size


y=np.zeros(n)

y[0]=1

for i in range(0,n-1,1):
	k0=h*f(x[i],y[i])

	k1=h*f(x[i]+h/2,y[i]+k0/2)
	
	k2=h*f(x[i]+h/2,y[i]+k1/2)
	
	k3=h*f(x[i]+h,y[i]+k2)
	
	y[i+1]=y[i]+(k0+2*k1+2*k2+k3)/6
	
	
	
#plt.plot((1+x)/(-1+x),y,"-b")
plt.plot(x,y,"-b")
plt.xlabel("$z$",fontsize=20)
plt.ylabel("x(z)",fontsize=20)
plt.show()

t=(3.5e06-1)/(3.5e06+1)

f = interpolate.interp1d(x, y)
print("solution(3.5e+06)=",f(t))

