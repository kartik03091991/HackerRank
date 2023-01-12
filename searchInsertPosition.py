
def searchInsert(nums: list[int], target: int) -> int:

        #nums = [1,3,5,6]
        nums = [1,3,5,6]
        target = 2
        #target = 5
        print(nums)
        print(target)
        
        #nums.append(target)
        print(nums)
        lst = []
        a = nums[-1]
        print(a)

        for x in range(0,len(nums)):
            if nums[x+1] - nums[x] != 0 and nums[x] < target < nums[x+1] and target not in nums:
                nums.insert(x+1,nums[x+1] -1)
                print(nums,"line1") 
                print(x+1, "final result")
            print(nums,"line2") 
        #nums.pop(-1)  
        print(nums,"line3")
        
        #for y in 
        

searchInsert([1,3,5,6],2)     
            