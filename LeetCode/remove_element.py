# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Remove Element
# problem url: https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums, val):
        while val in nums: nums.remove(val)
        return len(nums) 
        