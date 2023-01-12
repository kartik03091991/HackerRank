import math

#1 2 4 8 16

def print_formatted(number):
    #n = 17

    pad = n.bit_length()
    #print(pad)
    for i in range(1,n+1):
        pad = n.bit_length()
        a = int((i))
        b = oct(i)
        c = hex(i)
        d = bin(i)
        e = str(" ")
        #print(type(a))
        f =  str(a).rjust(pad)  + " " +  str(b[2:]).rjust(pad) + " " +  str(c[2:].upper()).rjust(pad) + " " +  str(d[2:]).rjust(pad)
        #f = str(a) + "  " +  str(b) + "  " +  str(c)+ " " +  str(d)
        print(f)
        #print(len(f))
        #print(lst1)
        #g = str(a) + " " +  str(b) + " " +  str(c) + " " +  str(d)
        #print(g)

#str(oct(i)[2:]).rjust(pad)   


#str4 = " ".join(lst1)
#print(str4)
#17    21    11 10001
#0o2 0x2 0b10
"""
t = str(" 17 21 11 10001")
m = list(t)
print(m)
l = " ".join(m)
#q = t.insert(1,"1")
print(l)
#print(q)
#print(t)
#print(len(t))
#print(lst1)
#lst2 = []

#for m in range(0,4):
  """  
    

    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)