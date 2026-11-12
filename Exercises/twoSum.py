def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True

    return False
    
"""The run time for this is Theta(n^2) because it loops over the list 2 times for each number"""
