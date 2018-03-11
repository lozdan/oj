# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Number of 1 Bits
# problem url: https://leetcode.com/problems/number-of-1-bits/description/

class Solution(object):
    def hammingWeight(self, n):
        answer = 0
        for _ in range(32):
            if n & 1 == 1:
                answer += 1
            n = n >> 1
        return answer
        