from collections import defaultdict 

class Solution(object):
    def key(self, s):
        base = ord('z') - ord('a')
        k = 0
        pow = 1
        for c in sorted(s):
            k += pow * (ord(c) - ord('a'))
            pow *= base
        return k
    
    def groupAnagrams(self, strs):
        groups = defaultdict(lambda: [])
        for s in strs:
            groups[self.key(s)].append(s)
        return groups.values()

m = Solution()
print(m)