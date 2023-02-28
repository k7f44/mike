import numpy as np 
import random 
a = np.array([random.randint(0, 100) for i in range(0, 100, 1)]) 

cnt = 0 
for a in a:
    if a > 50:
        cnt +=1 
print(cnt) 

a = np.array([random.randint(0, 100) for i in range(0, 100, 1)]) 
print ((a  > 50).sum())