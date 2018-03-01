# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Find All Numbers Disappeared in an Array
# problem url: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums):
        length = len(nums)
        nums = set(nums)
        answer = []
        for i in range(1, length + 1):
            if i not in nums:
                answer.append(i)
        return answer
        