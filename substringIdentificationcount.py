def count_substring(string, sub_string):
    #0,1,2,3,4,5,6

    #string = "ABCDCDC"
    #sub_string = "CDC"
    #string = "WoW!ItSCoOWoWW"
    #sub_string = "oW"
    #string = "AbBaAbBaAbBa"
    #sub_string = "Ab"
    
    x = string.find(sub_string)
    #x = string.find("CDC")
    #print(x)
    # x == 2 len(substring)+x == 3+2
    y = string[x:len(sub_string)+x]
    #print(y)
    count = 0
    if y == sub_string:
        count+=1 

    r = len(sub_string)+x-1
    #print(r)

    string2 = string[r:]
    z = string2.find(sub_string)
    #z = string2.find("CDC")
    #print(z)
    t = string2[z:len(sub_string)+z]
    #print(t)

    if t == sub_string:
        count+=1 
   
    u = r + z + len(sub_string)    
    #print(u)
    if u == len(string):
        return(count)
    else:  
        m = len(sub_string)+z-1
        #print(m)
        #print(string2)
        string3 = string2[m:]
        #print(string3)
        k = string3.find(sub_string)
        #z = string2.find("CDC")
        #print(k)
        o = string3[k:len(sub_string)+k]
        #print(o)

        if o == sub_string:
            count+=1 
        
        
        return(count)


    


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)