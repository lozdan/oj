# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Median of Two Sorted Arrays
# problem url: https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        x = sorted(nums1 + nums2)
        if len(x) & 1 == 1:
            return float(x[len(x) // 2])
        else:
            return (x[len(x) // 2] + x[len(x) // 2 - 1]) / 2
        