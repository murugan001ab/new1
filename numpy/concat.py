import numpy as np
a=[[1,2],
   [3,4]]
b=[[5,6],
   [7,8]]
c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        c[i][j]=a[i][j]
            
print(c)


