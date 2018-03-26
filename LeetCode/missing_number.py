# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Missing Number
# problem url: https://leetcode.com/problems/missing-number/description/

class Solution(object):
    def missingNumber(self, nums):
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)
