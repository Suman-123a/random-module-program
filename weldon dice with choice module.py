#weldons dice expt
import numpy as np
nn=[]
for i in range(13):
	nn.append(0)
for i in range(26306):
	k=0
	for j in range(12):
		x=np.random.choice([1,2,3,4,5,6])
		if x==4 or x==5:
			k=k+1	
	for h in range(13):
		if k==h:
			nn[h]=nn[h]+1
for i in range(13):
	w=nn[i]/26306
	print("success=",i,"P=",w)

			
			
			