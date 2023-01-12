if __name__ == '__main__':
    s = input()
    


#isalnum()
#isalpha()
#isdigit()
#islower()
#isupper()


a = s.isalnum()
b = s.isalpha()
c = s.isdigit()
d = s.islower()
e = s.isupper()    

#s = "qA2"

lst = list(s)

f = lst[1].isupper()
g = lst[0].islower()
h = lst[2].isdigit()
i = lst[0].isalpha()
j = s.isalnum()

xalnum = []
for o in range(0, len(lst)):
    if lst[o].isalnum():
        y = lst[o].isalnum()
        xalnum.append(y)
    else:
        xalnum.append(bool(False))
#print(xalnum)


if bool(True) in xalnum:
    print("True")
else:
    print("False")


xalpha = []
for m in range(0, len(lst)):
    if lst[m].isalpha():
        y = lst[m].isalpha()
        xalpha.append(y)
    else:
        xalpha.append(bool(False))
#print(xalpha)


if bool(True) in xalpha:
    print("True")
else:
    print("False")


xdigit = []
for n in range(0, len(lst)):
    if lst[n].isdigit():
        y = lst[n].isdigit()
        xdigit.append(y)
    else:
        xdigit.append(bool(False))
#print(xdigit)

if bool(True) in xdigit:
    print("True")
else:
    print("False")


xlower = []
for p in range(0, len(lst)):
    if lst[p].islower():
        y = lst[p].islower()
        xlower.append(y)
    else:
        xlower.append(bool(False))
#print(xlower)

if bool(True) in xlower:
    print("True")
else:
    print("False")


xupper = []
for q in range(0, len(lst)):
    if lst[q].isupper():
        y = lst[q].isupper()
        xupper.append(y)
    else:
        xupper.append(bool(False))
#print(xupper)


if bool(True) in xupper:
    print("True")
else:
    print("False")

"""
for xvar in range(0,len(xupper)):
    if xupper[xvar] == "True":
        True
"""
"""
print(f)
print(g)
print(h)
print(i)
print(j)
"""

"""
print(f)
print(lst)
print(a)
print(b)
print(c)
print(d)
print(e)

"""
    
    
    
    