#coin tossing
import matplotlib.pyplot as plt
import numpy as np
yy1=[]
for i in range(1000):
 k=0
 for j in range(10):
  r=np.random.rand()
  if 0<r<0.5:
   k=k+1
 yy1.append(k)
a=0
yy2=[]
for i in range(1000):
 a=a+yy1[i]
 av=a/(i+1)
 yy2.append(av)
plt.plot(yy1)
plt.plot(yy2)
plt.show()