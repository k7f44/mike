import numpy as np 
a = np.array([[4, 2], [9, 1]])
b = np.array([[5, 3], [2, 5]]) 

c= np.vstack((a, b)) 
print (c)

sr=c[:-1, 0]
print(sr)

srm=sr.max()
print(srm)

srm1=sr.min()
print(srm1)

srm2=sr.sum()
print(srm2)

d= np.hstack((a, b)) 
print (d)

srs=d[0, :-1]
print(' a' , srs)

srm=srs.max()
print(srm)

srm1=srs.min()
print(srm1)

srm2=srs.sum()
print(srm2)