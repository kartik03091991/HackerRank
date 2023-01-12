# Enter your code here. Read input from STDIN. Print output to STDOUT

lst = []

for x in range(0,4):
    lst.append(int(input()))
    
#print(lst)
a = lst[0]
b = lst[1]
c = lst[2]
d = lst[3]

s1 = a**b
s2 = c**d
s3 = s1 + s2
#print(s1)
#print(s2)
print(s3)