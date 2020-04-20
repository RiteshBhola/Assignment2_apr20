#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float fun(float x,float y)
{
	return(y-x*x+1);
}

float sol(float x)
{
	return((x+1)*(x+1)-0.5*exp(x));
}


void main()
{
	 int a=0,b=2;
	 float h=0.2;
	 int n= (b-a)/h + 1;
	 float *y,*x,*yreal,*error,*error_bound;
	 float L=1.0,M=fabs(0.5*exp(1)*exp(1)-2);
	 
	 y=(float*)malloc(n*sizeof(float));
	 x=(float*)malloc(n*sizeof(float));
	 yreal=(float*)malloc(n*sizeof(float));
	 error=(float*)malloc(n*sizeof(float));
	 error_bound=(float*)malloc(n*sizeof(float));
	 
	 y[0]=0.5;
	 x[0]=0;
	 yreal[0]=sol(x[0]);
	 error[0]=fabs( y[0]-yreal[0]);
	 error_bound[0]=((h*M)/(2*L))*(exp(L*(x[0]-a))-1);
	 
	 printf("w(t) - solution from euler method\n"); 
	 printf("y(t) - analytical solution \n"); 
	 printf("----------------------------------------------------------------------\n");
	 printf("    t        w(t)         y(t)       |y(t)-w(t)|       Error bound\n");
	 printf("======================================================================\n");
	 printf("%f   %f    %f       %f          %f\n",x[0],y[0],yreal[0],error[0],error_bound[0]);
	 for(int i=0;i<n-1;i++)
	 {
	   x[i+1]=x[i]+h;
	   y[i+1]=y[i]+h*fun(x[i],y[i]);
	   yreal[i+1]=sol(x[i+1]);
	   error[i+1]=fabs( y[i+1]-yreal[i+1]);
	   error_bound[i+1]=((h*M)/(2*L))*(exp(L*(x[i+1]-a))-1);
	   printf("%f   %f    %f       %f          %f\n",x[i+1],y[i+1],yreal[i+1],error[i+1],error_bound[i+1]);
	 }
	 
	 free(y);
	 free(x);
	 free(yreal);
	 free(error);
}
