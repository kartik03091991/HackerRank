# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())

lst = []

lsthead = []
lsthead.append(list(map(str,input().split())))
#print(lsthead)

for x in range(0,N):
    lst.append(list(map(str,input().split())))
    
#print(lst)
#print(lsthead[0][1])
#taking the index for the marks 
for x in range(0,len(lsthead[0])):
    if lsthead[0][x] == "MARKS":
        c = x
#print(c)

#getting the total from thr main list
total = 0
for x in range(0,N):
    total += int(lst[x][c])
    
#print(total)

#getting the average
average = total/N
print(average)


"""

TESTCASE 01

5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
TESTCASE 02

5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
Sample Output

TESTCASE 01

78.00
TESTCASE 02

81.00

"""

