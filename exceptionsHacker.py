# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
#print(a)
#lst1 = list(map(str,input().split()))
#print(lst1)

#lst2 = list(map(str,input().split()))
#print(lst2)

#lst3 = list(map(str,input().split()))
#print(lst3)

lst4 = []
for x in range(0,a):
    lst4.append(list(map(str,input().split())))

#print(lst4)
#print(len(lst4))
#print(lst4[0])

"""
try:
  print(int(lst4[0][0])/int(lst4[0][1]))
except ZeroDivisionError:
  print("Error Code: integer division or modulo by zero")
    
try:
  print(int(lst4[1][0])/int(lst4[1][1]))
except ValueError:
  print("Error Code: invalid literal for int() with base 10:",lst4[1][1])
"""    
for x,y in lst4:
    #print(x,y)
    try:
       print(int(int(x)/int(y)))
    except ZeroDivisionError:
       print("Error Code: integer division or modulo by zero")
    except ValueError:
       if x == '#':
          print("Error Code: invalid literal for int() with base 10:","'"+x+"'")
       else:
          print("Error Code: invalid literal for int() with base 10:","'"+y+"'")
"""        
        if ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
        elif ValueError:
            print("Error Code: invalid literal for int() with base 10:",y)  
        else:
            print(int(x)/int(y))  
"""            
            
"""                
    try:
       print(int(x)/int(y))
    except ValueError:
       print("Error Code: invalid literal for int() with base 10:",lst4[1][1])
"""
       
    
    