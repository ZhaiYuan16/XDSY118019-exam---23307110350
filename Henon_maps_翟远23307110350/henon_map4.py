import matplotlib.pyplot as plt
# input section
a=0.8975
b=0.3
x=[0]
y=[0]
N=int(input('N='))

# computing section
for i in range(N):
    x_next=1-a*x[i]**2+y[i]
    y_next=b*x[i]
    x.append(x_next)
    y.append(y_next)




# output section
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
print(x)