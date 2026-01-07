# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):

        indices_of_sum = {}

        for i, num in enumerate(nums):
            if target - num in indices_of_sum:
                return [indices_of_sum[target - num], i]
            indices_of_sum[num] = i