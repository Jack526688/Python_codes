def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                print(nums)


nums = [5, 8, 1, 7, 9, 3, 0]

sort(nums)

print(nums)
