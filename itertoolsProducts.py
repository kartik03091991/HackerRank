"""
x, y = map(int, input().split())
It works as follows:

input() will query the user for input, and read one line of user input;
.split() will split that input into a list of “words”;
map(int, ...) will call int on each word, it will to that lazily (although that is not important here); and
x, y = ... will unpack the expression into two elements, and assign the first one to n and the second one to S.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

# store the input in a list  A and B 
# then use the product function for  A and B 

from itertools import product

#p1 = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19"
#q1 = "0 1"


a = list(map(int,input().split()))
b = list(map(int,input().split()))



"""
input1 =  list(input())

lst = []

lst.append(input1)
lst.append(list(input()))
"""

"""
input1 =  list(p)

lst = []

lst.append(input1)
lst.append(list(q))


print(lst)

A = []
B = []

A.append(lst[0])
B.append(lst[1])

C = tuple(A[0])
D = tuple(B[0])

A = list(C)
B = list(D)

print(A)
print(B)

lstA = []


for x in range(len(A)):
    if A[x] != " ":
        lstA.append(int(A[x]))


#print(lstA)


lstB = []


for x in range(len(B)):
    if B[x] != " ":
        lstB.append(int(B[x]))

"""
#print(lstB)

#print(list(product(lstA,lstB)))

R = list(product(a,b))


T = tuple(R)
#print(T)
#print(len(T))

for x in T:
    print(x , end = " ")
    



"""
for x in range(len(A)):
    if A[x] == " ":
        lstA.append(" "+A[x+1])
    else:
        lstA.append(A[x])
"""


"""
a = list(" ".join(lst))
print(a)
A = []
B = []
for x in range(len(lst)):
    if x == 0:
        A.append(lst[x])
    else:
        B.append(lst[x])
    
print(A)
print(B)

print(" ".join(lst))
"""
