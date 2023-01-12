nums = [4,3,6,16,8,2]

nums.sort(reverse=True)

d = {}

for i in nums:
    print(d.get(i*i,0))
    d[i] = d.get(i*i,0) + 1
    print(d[i])

print(d)

print(max(d.values()))