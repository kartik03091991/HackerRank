class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #s = "Hello World"
        #s = "   fly me   to   the moon  "
        
        #lst1 = list(map(str,s.split()))
        #print(lst1)
        
        #return(len(lst1[-1]))
        #lst1 = list(map(str,s.split()))
        #print(lst1)
        
        #return(len(list(map(str,s.split()))[-1]))
        return(len(list(s.split())[-1]))
    
"""  
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
"""  