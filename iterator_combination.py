# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations
S, k = input().split()
S = ''.join(sorted(S))
for i in range(1, int(k)+1):
    comb = list(combinations(S, i))
    for v in comb:
        print(*v, sep="")

from itertools import combinations

a = list(map(str,input().split()))

#print(a)

b = list(a[0])
c = int(a[1])

#print(b)
#print(c)

p = []
r1 = []
for x in range(1,c+1):
    f1 = list(combinations(b,x))
    f1.sort()
    for x in range(0,len(f1)):
        e = sorted(f1[x])
        p.append("".join(e))
        p.sort()
        #print(p)
        r1.append(p)
        r1.sort()
        print(r1)
        #print("\n".join(p))
        #r = "\n".join(p)
        #print(sorted(r))
        p.clear()
r1.clear()    
"""       
 e = sorted(d[x])
    r.append("".join(e))

print("\n".join(p))
r.sort()
print("\n".join(r))
"""
"""

d = list(combinations(b,c))
d.sort()
#print(d)
#print(len(d))

f = list(combinations(b,c-1))
f.sort()
#print(f)


p = []
for x in range(0,len(f)):
    e = f[x]
    p.append("".join(e))
    

#m = []
#m = d[0]
#print("".join(m))
 
r = []

for x in range(0,len(d)):
    e = sorted(d[x])
    r.append("".join(e))

print("\n".join(p))
r.sort()
print("\n".join(r))
    
"""


