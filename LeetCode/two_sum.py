# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Two Sum
# problem url: https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums, target):
        y = {}
        for i in range(len(nums)):
            if target - nums[i] in y:
                return sorted([i, y[target - nums[i]]])
            y[nums[i]] = i
