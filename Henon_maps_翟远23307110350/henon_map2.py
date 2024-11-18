import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# input section
a=1.4
b=0.3
N=int(input('N='))
# computing section
while N:
    x=[0]
    y=[0]
    for i in range(N):
        x_next=1-a*x[i]**2+y[i]
        y_next=b*x[i]
        x.append(x_next)
        y.append(y_next)
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    x.clear()
    y.clear()
    N=int(input('N='))
    
# enter '0' to end the program
# and please click off the diagram after viewing