n = int(input())
s = set(map(int, input().split()))

#print(n)
#print(s)
N = int(input())

lst = []
for x in range(0,N):
    lst.append(list(map(str,input().split())))
    

#print(lst)
#print(len(lst))
#print(lst[0][0])
#print(lst[1][1])
 
y = 1
for x in range(0,len(lst)):
    if lst[x][0] == "pop":
        s.pop()
        #print(s,"line1")
    if lst[x][0] == "remove":
        s.remove(int(lst[x][y]))
        #print(s,"line2")
    if lst[x][0] == "discard":
        s.discard(int(lst[x][y]))
        #print(s,"line3")    
#s.sum()
#print(s.pop()) 

lst2 = list(s)
total = 0

if len(lst2) == 1:
    print(s.pop())
else:
    for x in range(0,len(lst2)):
        total += lst2[x]
    print(total)
