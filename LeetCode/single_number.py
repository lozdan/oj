# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Single Number
# problem url: https://leetcode.com/problems/single-number/description/

class Solution(object):
    def singleNumber(self, nums):
        count = 0
        for c in nums:
            count ^= c
        return count
        