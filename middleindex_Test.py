nums = [1,7,3,6,5,6]


if len(nums) == 0:
    print(-1)
left = [0, nums[0]]
right = [0, nums[-1]]

print(left)
print(right)
for i in range(1, len(nums) - 1):
    left.append(nums[i] + left[-1])
    right.append(nums[len(nums) - 1 - i] + right[-1])
    print(left,'left')
    print(right,'right')
right = right[::-1]
print(right,'right2')
for i in range(len(left)):
    if left[i] == right[i]:
        print( i)
print( -1)



