class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst1 = ["Fizz","Buzz","FizzBuzz"]
        lst2 = list(enumerate(lst1))
        var1 = []
        #print(lst2)
        lst3 = []
        #n = 15
        for x in range(1,n+1):
            lst3.append(str(x))
        
        #print(lst3)
        
        #print(lst3[4])
        #m = int(lst3[4]) % 3 
        #print(m)
        
        lst4 = []

  
        for x in range(0,len(lst3)):
            if int(lst3[x]) % 3 == 0:
                #lst3.remove(lst3[x])
                lst4.append("Fizz")
                #print(lst4, "line1")
            if int(lst3[x]) % 5 == 0:
                #lst3.remove(lst3[x])
                lst4.append("Buzz")
                #print(lst4, "line2")
            #if int(lst3[x]) % 3 == 0 and int(lst3[x]) % 5 == 0 :
            if int(lst3[x]) % 15 == 0 :
                lst4.pop(x)
                lst4.pop(x)
                lst4.append("FizzBuzz")
                #print(lst4, "line3")
            if int(lst3[x]) % 3 != 0 and int(lst3[x]) % 5 != 0 and int(lst3[x]) % 15 != 0:
                lst4.append(lst3[x])
                #print(lst3[x], "line4")
                #print(lst4,"line4")
        #print(lst4 , "line5")
        return(lst4)

        
"""
            if lst3[x] % 3 == 0:
                lst3.remove(lst3[x])
                lst3.append("Fizz")
            else:
                lst3.remove(lst3[x])
                lst3.append(lst3[str(x)])
"""
        
        
        