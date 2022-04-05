import numpy as np
from time import process_time_ns as ns


def max(v):
    m = v[0]  #(1)
    for i in range(1, len(v)):  #(2)
        if v[i] > m:  #(3)
            m = v[i]  #(4)
    return m  #(5)

v = np.random.randint(1, 100, 100)
s = sorted(v)
x = sorted(v, reverse=True)

n1 = ns()
m = max(v)
n2 = ns()

print(n2-n1)

def bubbleSort(v):
    n = len(v)

    for i in range(n-1):
 
     
        for j in range(0, n-i-1):
 
            if v[j] > v[j + 1] :
                v[j], v[j + 1] = v[j + 1], v[j]

 
bubbleSort(v)
 
print (":")
for i in range(len(v)):
    print ("% d" % v[i],end=" ")