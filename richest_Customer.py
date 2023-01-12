class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        print(accounts)
        total = 0
        lst = []
        for x in range(0,len(accounts)):
            for y in accounts[x]:
                print(y)
                total+=y
            print(total)
            lst.append(total)
            print(lst)
            total = 0
        
        print(max(lst))