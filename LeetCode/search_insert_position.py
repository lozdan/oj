# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Search Insert Position
# problem url: https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
        return len(nums)
            