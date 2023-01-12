from collections import Counter
X=int(input())
Y=Counter(map(int,input().split()))
N=int(input())     # Number of customers
total=0
for i in range (N):
    size,price=map(int,input().split())
    if Y[size]:
        total+=price
        Y[size]-=1
print(total)

"""
Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200
"""