# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import cmath

num1 = list(map(str,input().split()))
#num = "-1-5j"
#num1 = list(map(str,"-1-5j".split()))
#print(num1)

#z1 = z1.real + z1.imag*1j = input()

A = "".join(num1)

#print(A)
z1 =  complex(A)
z1 = z1.real + z1.imag*1j 
 
#print(z1)
#print(z1.real)
#print(z1.imag)

#lst1 = []

"""
for x in range(len(A)):
    lst1.append(A[x])
    
print(lst1)

x = int(lst1[0])
y = int(lst1[2])

#print(x)
#print(y)
"""

xsquare = abs(z1.real)**2
ysquare = abs(z1.imag)**2
#print(xsquare+ysquare)
z = math.sqrt(abs(xsquare)+abs(ysquare))
print(z)
print(cmath.phase(complex(z1.real,z1.imag)))



