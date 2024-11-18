import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x=[]
y=[]
u=[]

# input section
a=eval(input('a='))
b=eval(input('b='))
u0=input('u0=') #only use space to seperate x and y coordinates
N=int(input('N='))
m=u0.split()
x0=eval(m[0])
y0=eval(m[1])
x.append(x0)
y.append(y0)
u.append((x0,y0))

# computing section
for i in range(N):
    x_next=1-a*x[i]**2+y[i]
    y_next=b*x[i]
    x.append(x_next)
    y.append(y_next)
    u.append((x_next,y_next))

# output section
print(u)