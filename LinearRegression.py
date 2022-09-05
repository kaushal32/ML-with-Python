X = [171,151,124,134,156]
Y = [80,60,45,50,65]
n = len(X)
print(n)
mean_x = sum(X)/n
mean_y = sum(Y)/n
print(mean_x)
print(mean_y)
p=0;
z=0;
for i in range(n):
  p+= (X[i]-mean_x) *(Y[i]-mean_y)

for i in range(n):  
  z+= (X[i]-mean_x)**2;
m=p/z;
c=mean_y-(m*mean_x)
print(m)
print(c)
F=m*130+c;
print(F)

import matplotlib.pyplot as plt
plt.scatter(X,Y)
plt.plot(X,Y)
plt.show()

import numpy as np 
import matplotlib.pyplot as plt
max_x=np.max(X)+100
min_x=np.min(X)-100

x=np.linspace(min_x,max_x,100)
y=[]
for i in range(100):
  y.append(c+m*x[i])
plt.scatter(X,Y, Color = 'orange')
plt.plot(x,y)
