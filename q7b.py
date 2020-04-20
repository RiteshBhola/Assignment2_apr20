import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 


def fun(t,y):
	return(1-(t-y)**2)
	
y0=0
h=0.01
tspan=np.arange(2,3+h,h)
n=tspan.size

sol=solve_ivp(fun,[tspan[0],tspan[n-1]],[0],t_eval=tspan)

m=sol.y[0,:]
plt.plot(sol.t,m,"-k",label="numpy.solve_ivp solution\nSolution in not converging")
plt.xlabel("$x$",fontsize=20)
plt.ylabel("y(x)",fontsize=20)
plt.legend()
plt.show()
if(sol.status==-1):
 print("not converging")
