import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# input section
a_min=eval(input('the minimum of a='))
a_max=eval(input('the maximum of a='))
a_step=eval(input('the step of a ='))
b=0.3
N=int(input('N='))
# computing section
a_list=np.arange(a_min,a_max+a_step,a_step).tolist()
for a in a_list:
    x=[0]
    y=[0]
    for i in range(N):
        x_next=1-a*x[i]**2+y[i]
        y_next=b*x[i]
        x.append(x_next)
        y.append(y_next)
    plt.scatter([a]*(N+1),x,s=1)
    x.clear()
    y.clear()

#output section
plt.xlabel('a')
plt.ylabel('x')
plt.show()