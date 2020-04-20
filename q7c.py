import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 


def fun(t,y):
	return(1+y/t)
	
def g(x):
	return(2*x+x*np.log(x))
y0=2
h=0.01
tspan=np.arange(1,2+h,h)
n=tspan.size

sol=solve_ivp(fun,[tspan[0],tspan[n-1]],[2],t_eval=tspan)
print(sol.t)
print(sol.y)
m=sol.y[0,:]
plt.plot(sol.t,m,"-k",label="From numpy.solve_ivp")
plt.plot(sol.t,g(sol.t),"*r",label="From symbolic calculator")

plt.xlabel("$x$",fontsize=20)
plt.ylabel("y(x)",fontsize=20)
plt.legend()
plt.show()
plt.show()
if(sol.status==-1):
 print("not converging")
