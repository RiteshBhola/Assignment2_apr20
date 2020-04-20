import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 


def solution(t):
	return((t/5)*np.exp(3*t) - (1/25)*np.exp(3*t) + (1/25)*np.exp(-2*t))

def fun(t,y):
	return(t*np.exp(3*t)-2*y)
	
y0=0
h=0.001
tspan=np.arange(0,1+h,h)
n=tspan.size

sol=solve_ivp(fun,[0,1],[0],t_eval=tspan)
print(sol.t)
print(sol.y)
m=sol.y[0,:]
x=sol.t
plt.plot(sol.t,m,label="From numpy.solve_ivp")
x=np.arange(0,1+h,10*h)
plt.plot(x,solution(x),"*k",label="From symbolic calculator")
plt.xlabel("$x$",fontsize=20)
plt.ylabel("y(x)",fontsize=20)
plt.legend()
plt.show()
if(sol.status==-1):
 print("not converging")
