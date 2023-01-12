import textwrap

def wrap(string, max_width):
    #string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"   
    #max_width = 4

    lst1 = list(string)

    lst = []
    x = 1

    #print(lst1)

    g = len(string) % max_width
    #print(g)  
    
    h = []
    
    for i in range(0,len(string)):
        lst.append(lst1[i])
        y = len(lst)
        if y == max_width:
           #m.append(lst)
           #b = print("".join(lst))
           h.append(lst[0:max_width])
           lst.clear()

    f = len(string) - g
    #print(f)
    #print(h)
    length_h =  len(h)
    
    u = []
    r = []
    for q in range(0,len(h)):
        r = "".join(h[q])
        u.append(r)
        
        
    #print(u)
    #print(r)
    
    g = []
    #for w in range(0,len(u)):
        #g = "".join(u[w])
        
    result = "\n".join(u) +"\n"+"".join(lst1[f:])    
    #print(g)
    

        
    
    #result1 = "".join(lst1[f:])
    
    return(result)
    #print(result1)
    #lst3 = list(b)
    
    #print(lst3)
    
    
    




if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)