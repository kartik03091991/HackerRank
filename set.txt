# Enter your code here. Read input from STDIN. Print output to STDOUT

lst = []

for x in range(0,int(input())):
    lst.append(input())
    
#print(lst)
set1 = set(lst)
#print(set1)
print(len(set1))