import numpy as np
import matplotlib.pyplot as plt


h=0.1
x=np.arange(1,2+h,h)

print(x)
n=np.size(x)
print(n)
y=np.zeros(n)
y[0]=1

def solution(t):
	return(t/(1+np.log(t)))


def fun(y):
	return((y/t) - (y/t)**2)





for i in range(0,n-1,1):
	t=x[i]
	y[i+1]=y[i]+h*fun(y[i])


abs_err=np.abs(y-solution(x))
rel_err=abs_err/solution(x)


print("absolute error\n",abs_err)
print("relative error\n",rel_err)
plt.plot(x,y,"*r",label="Euler's method")
x=np.arange(1,2+h,0.1*h)
plt.plot(x,solution(x),"-b",label="Analytic Solution")
plt.xlabel("$x$",fontsize=20)
plt.ylabel("y(x)",fontsize=20)
plt.legend()
plt.show()
