from google.colab import files
uploaded = files.upload()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from subprocess import check_output

data = pd.read_csv('headbrain.csv')


X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values
n = len(X);
mean_X = sum(X)/n;
mean_Y = sum(Y)/n;
num = 0;
deno = 0;
for i in range(n):
    num += (X[i] - mean_X)*(Y[i]-mean_Y);
    deno += (X[i] - mean_X)**2;
m = num/deno;
c = mean_Y - m * mean_X;
print(m);
print(c);


import matplotlib.pyplot as plt
plt.scatter(X,Y)
plt.plot(X,Y)
plt.show();


import matplotlib.pyplot as plt
import numpy as np
max_x = np.max(X)+100;
min_x = np.min(X)-100;

x = np.linspace(min_x, max_x, 100)
y = []
for i in range(100):
  y.append(c + m*x[i])
plt.plot(x,y);
plt.scatter(X,Y,color = 'orange');
