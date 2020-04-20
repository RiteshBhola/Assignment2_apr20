import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


h=0.01
x=np.arange(0,1,h)
n=int((x[np.size(x)-1]-x[0])/h)+1

y=np.zeros(n)
y[0]=1/3.0

	

def fun(w):
	return(w-h*( - 20*(w-t)**2 + 2*t )-p)

def fp(w):
	der=1.0+h*40*(w-t)
	return der

for i in range(0,n-1,1):
	t=x[i]
	p=y[i]
	sol = optimize.root_scalar(fun, x0=y[i] ,fprime=fp, method='newton')
	#sol= optimize.fsolve(fun,p)
	y[i+1]=sol.root



ym=fun(x)
plt.plot(x,y,".-r")
plt.xlabel("$x$",fontsize=20)
plt.ylabel("y(x)",fontsize=20)
plt.show()
