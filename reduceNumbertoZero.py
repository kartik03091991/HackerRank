class Solution:
    def numberOfSteps(self, num: int) -> int:
        #print(num)
        x = 0
        step = 0
        #num = 8
        total = 0
        while x <= num:
           #num-=1 
           if num % 2 == 0 and num != 0.0:
              num =  num/2
              #print(num, "line1")
              #num-=1
              step+=1  
           elif num % 2 != 0 and num != 0.0:
              #print(num,"between line 1 and 2")
              num-=1
              #print(num,"line2")
              step+=1
           #num-=1
           elif num == 0.0:
                break
        return(step)
            