def sort(nums):

    for i in range(len(nums)):
        k = i
        for j in range(i, len(nums)):
            if nums[j] < nums[k]:
                k = j

        nums[i], nums[k] = nums[k], nums[i]
        print(nums)


nums = [5, 99, 8, 1, 7, 9, 3, 0, 1]

sort(nums)

print(nums)
