#find first missing positive integer

nums = [3, 4, -1, 1]
n = len(nums)

for i in range(n):

    while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:

        correct_index = nums[i] - 1
        nums[i], nums[correct_index] = nums[correct_index], nums[i]

print(nums)

for i in range(n):
    if nums[i] != i + 1:
        print(i + 1)
        break
else:
    print(n + 1)