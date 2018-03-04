# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Remove Duplicates from Sorted Array
# problem url: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums):
        x = sorted(list(set(nums)))
        for i in range(len(x)):
            nums[i] = x[i]
        return len(x)
