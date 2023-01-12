# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict
from collections import Counter

N = int(input())
ord1 = OrderedDict()
dict1 = {}
lst1 = []

for x in range(0,N):
    lst1.append(input().split())
    
#print(lst1)

#print(lst1[0])
lst2 = []

for x in range(0,len(lst1)):
    if len(lst1[x]) > 2:
        lst2.append(lst1[x][0:len(lst1[x])-1])
        #print(lst2)
    if len(lst1[x]) <= 2:
        lst2.append(lst1[x][0:1])
        #print(lst2)

#print(lst2)

lstprice = []
for x in range(0,len(lst1)):
    lstprice.append(int(lst1[x][-1]))
    
#print(lstprice) 

a = lst1[0][0:2]
#print(a)
b = " ".join(a)
#print(b)

c = " ".join(lst1[0][0:2])
#print(c)

lstitems = []

for x in range(0,len(lst2)):
    if len(lst2[x]) > 1:
        d = " ".join((lst2[x][0:len(lst2)]))
        #print(lst2)
        lstitems.append(d)
    if len(lst2[x]) == 1:
        d = " ".join((lst2[x]))
        #print(lst2)
        lstitems.append(d)        
#print(lstitems)

lstunq = []

for x in range(0,len(lstitems)):
    if lstitems[x] not in lstunq:
        lstunq.append(lstitems[x])

#print(lstunq)

lsttotal = []
count1 = 0
for x in range(0,len(lstunq)):
    for y in range(0,len(lstitems)):
        if lstunq[x] == lstitems[y]:
            count1 += lstprice[y]           
    lsttotal.append(count1)
    #print(lsttotal)
    count1 = 0        

for x in range(0,len(lstunq)):
    print(lstunq[x],lsttotal[x])
    
"""
Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
"""