# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Majority Element
# problem url: https://leetcode.com/problems/majority-element/description/

class Solution(object):
    def majorityElement(self, nums):
        nums = sorted(nums)
        return nums[len(nums)//2]
        
