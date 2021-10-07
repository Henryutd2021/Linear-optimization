import random as rd
import numpy as np


a = 0.1
b = 0.2
#i = 0
count = 0
k = range(50000)
for i in k:
    r1 = rd.random()
    r2 = rd.random()
    x = -1*(np.log(1-r1))/a
    y = -1*(np.log(1-r2))/b
    #print(x, y)
    if x < y:
        count += 1
    # else:
    #     count += 0
   # i += 1
print(float(count/len(k)))
