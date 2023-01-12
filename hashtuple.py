

tup1 = ('1','2')

print(tup1)

str1 = tup1[0]
str2 = ' '
str3 = tup1[1]

str4 = str1+str2+str3
print(len(tup1))
print(str4)
print(hash(str4))
print(hash(len(tup1)))

n = int(input())
t = tuple(map(int, input().split(' ')))
print(hash(t))