lst1 = []
lst1.insert(0,5)
lst1.insert(1,10)
lst1.insert(0,6)
print(lst1)
lst1.remove(6)
lst1.append(9)
lst1.append(1)
lst1.sort()
print(lst1)
lst1.pop()
lst1.reverse()
print(lst1)

i = 0
e = 1

lst2 = ['.insert(i,e)','\nprint','.remove(e)','.append(e)','.sort','.pop','.reverse']
print(lst2)
a = lst2[0]
b = lst2[1]
c = lst2[2]
d = lst2[3]
e = lst2[4]
f = lst2[5]
g = lst2[6]


lst3 = []

for x in lst2:
    if   a == '.insert(i,e)':
        lst3.insert(0,1)
    if b == '\nprint':
        print(lst3)
    if c == '.remove(e)':
        lst3.remove(1)
    if d == '.append(e)':
        lst3.append(1)
    if e == '.sort':
        lst3.sort()
    if f == '.pop':
        lst3.pop()
    else: 
        lst3.reverse()  

print(lst3)



if __name__ == '__main__':
    lst = []
    N = int(input())
    for cmd_number in range(N):
        cmd,*arg = input().split()
        arg = [int(str_val) for str_val in arg]
        
        
        if cmd == "insert":
            lst.insert(arg[0],arg[1])
        elif cmd == "print":
            print(lst)
        elif cmd == "remove":
            lst.remove(arg[0])
        elif cmd == "append":
            lst.append(arg[0])
        elif cmd == "sort":
            lst.sort()
        elif cmd == "pop":
            lst.pop()
        elif cmd == "reverse":
            lst.reverse()