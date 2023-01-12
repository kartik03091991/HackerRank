# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

a = list(map(str,input().split()))

#print(a)

b = list(a[0])
c = int(a[1])

#print(b)
#print(c)

d = list(permutations(b,c))
d.sort()
#print(d)
#print(len(d))

#m = []
#m = d[0]
#print("".join(m))
e = []

for x in range(0,len(d)):
    e = d[x]
    print("".join(e))
    

