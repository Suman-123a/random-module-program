#weldons dice
import numpy as np
nn=[]
b=1/6
for i in range(13):
	nn.append(0)
for i in range(26306):
	k=0
	for j in range(12):
		r=np.random.rand()
		if 3*b<r<5*b:
			k=k+1	
	for h in range(13):
		if k==h:
			nn[h]=nn[h]+1
for i in range(13):
	w=nn[i]/26306
	print("success=",i,"P=",w)
print("corresponding binomial distribution result:")
def f(m):
	fact=1
	for i in range(1,m+1):
		fact=fact*i
	return fact
def nCr(n,r):
	z=f(n)/(f(n-r)*f(r))
	return z
for i in range(13):
	d=nCr(12,i)*(1/3)**i*(2/3)**(12-i)
	print(d)

			
			
			