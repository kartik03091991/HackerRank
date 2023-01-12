# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

K = int(input())
lst = Counter(input().split())

#print(lst)
print(lst.most_common()[-1][0])
#print(room.most_common()[-1][0])

"""
count = 0
lst2 = []
for x in range(0,len(lst)):
      lst2.append(lst[x])
"""     
        
"""
for x in range(0,len(l1)):
    if lst.count(l1[x]) == 1:
        print(l1[x])
        break
"""
