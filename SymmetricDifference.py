# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input())
lsta = list(map(int,input().split()))
a = set(lsta)
N = int(input())
lstb = list(map(int,input().split()))
b = set(lstb)

#print(M)
#print(a)
#print(N)
#print(b)

a_union_b = a.union(b)
#print(a_union_b)
a_intersection_b = a.intersection(b)
#print(a_intersection_b)

c = a_union_b.difference(a_intersection_b)
#print(c)
d = list(c)
d.sort()
for x in range(0,len(d)):
    print(d[x])

