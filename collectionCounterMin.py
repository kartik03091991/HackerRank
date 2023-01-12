class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        #lst = []
        #lst = list(enumerate(nums))
        #print(lst)
        num1 = Counter(nums)
        #print(num1)
        #print(num1.elements() ) 
        #a = {}
        #a = num1.values()
        #print(a)
        return(min(num1, key=num1.get))

        
            
# second solution
# 
# 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        stack=[]
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i] not  in stack :
                stack.append(nums[i])
            else:
                stack.pop()
        return stack[0]            
            
            
            
        