# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

N = int(input())
lst = []

for x in range(0,N):
    lst.append(list(map(str,input().split())))
    
    
#print(lst)

lstop = []
lstnum = []

for x in range(0,len(lst)):
    lstop.append(lst[x][0])
    #lstnum.append(lst[x][1])
    
#print(lstop)
#print(lstnum)

for x in range(0,len(lstop)):
    if lstop[x] == "pop" or lstop[x] == "popleft":
        lstnum.append(lst[x])
    else:
        lstnum.append(lst[x][1])
        
#print(lstnum)

d = deque()

for x in range(0,len(lstop)):
    if lst[x][0] == "pop":
        d.pop()
    if lst[x][0] == "popleft":
        d.popleft()
    if lst[x][0] == "append":
        d.append(lstnum[x])
    if lst[x][0] == "appendleft":
        d.appendleft(lstnum[x])
    if lst[x][0] == "extend":
        d.extend(lstnum[x])
    if lst[x][0] == "remove":
        d.remove(lstnum[x])    
    if lst[x][0] == "reverse":
        d.reverse(lstnum[x])
    if lst[x][0] == "rotate":
        d.rotate(lstnum[x])          

#print(d)

for x in d:
    print(x,end = " ")

"""

for x in range(0,len(lstop)):
    if lst[x][0] == "pop" or lst[x][0] == "popleft":
        a = lst[x][0]
        print(a,"print a")
    else:
        b = lst[x][0]
        c = lst[x][1]
        print(b,"print b")
        print(c,"print c")
        #print(d+"."+b+"("+c+")")
        d
print(d)

"""

