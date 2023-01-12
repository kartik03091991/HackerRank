
lst = []
lst1 = []
y = 0
for x in range(1,3):
    lst.append(x)
    print(lst,"line1")
    while y <= x:
        lst1.append(lst[x-1])
        y+=1
        print(lst1,"line2")

print(lst)
print(lst1)