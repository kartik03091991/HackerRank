# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
lst = list(map(int,input().split()))
#print(all(lst))
#print(lst[0][0])

lst2 = []
for x in range(0,N):
    if lst[x]>0:
        lst2.append(True)
    else:
        lst2.append(False)

#print(lst2)
        
lst4 = []
for x in range(0,N):
    if 0< lst[x] < 10: 
       lst3 = []
       lst5 = []
       n1 = lst3.append(lst[x])
       n2 = lst3.reverse()
       if n1 == n2:
         lst4.append(True)        
    if lst[x] > 10:
        a = lst[x]/10
        #print(str(a))
        #print(str(a).split("."))
        s1 = list(str(a).split("."))
        #print(s1)
        s2 = list(s1)
        s2.reverse()
        #s2 = s1.reverse()       
        #print(s2)
        if s1 != s2:
            lst4.append(False)
        else:
            lst4.append(True)
#print(lst4) 

#print(all(lst2))
#print(any(lst4))

if all(lst2) and any(lst4):
    print(True)
else:
    print(False)




