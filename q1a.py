import numpy as np
import matplotlib.pyplot as plt
h=0.001
x=np.arange(0,1+h,h)
n=x.size
y=np.zeros(n)
y[0]=np.exp(1)


def fun(x):
	return(np.exp(-9*x+1))


for i in range(0,n-1,1):
	y[i+1]=y[i]/(1+9*h)


plt.plot(x,y,label="Euler Method")
x=np.arange(0,1+h,10*h)
ym=fun(x)
plt.plot(x,ym,"*r",label="Analytic Solution")
plt.xlabel("$x$",fontsize=20)
plt.ylabel("y(x)",fontsize=20)
plt.legend()
plt.show()
