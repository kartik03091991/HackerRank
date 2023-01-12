# Enter your code here. Read input from STDIN. Print output to STDOUT



#N = (5 < w < 101)
#M = (15 < r < 303) 
#print(N)
#print(M)

#21 - 3
#9 3 9
#21-3 = 18 /2 = 9

#N = 7
#M = N*3
finput = input()
lgt = len(finput)
lst3 = []
lst4 = list(finput)
#print(lgt)
lst5 = []

for x1 in range(0,len(lst4)):
    if lst4[x1].isspace() == True:
        lst3.append(lst4[x1+1:])
        lst5.append(lst4[:x1]) 
        
#bool(re.search(r"\s", test_str))
#print(lst3)


#print(lst4)
#print(lst3)
#print(lst5)

N = int("".join(lst5[0]))
M = int("".join(lst3[0]))
#print(N)
#print(M)

#N = int(finput[0])
#M = int(finput[2:])

"""
for p in range(6,102):
    print(p)
    q = p
"""
         
 
c1 = "-"
c2 = ".|."
c3 = "WELCOME"
#print(c3.ljust(21, '-'))

l = c3.center(21,c1)
#print(l)

f = (c2*2).center(21,c1)
#print(f)
y = 1
for x in range(0,N):
    if x < int((N/2)):
        k = (c2*y).center(M,c1)
        print(k)
        y+=2
    elif x > int(N/2)  :
        y-=2
        h = (c2*y).center(M,c1)
        print(h)
    else:
        i = c3.center(M,c1)
        print(i)
        
