# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Binary Number with Alternating Bits
# problem url: https://leetcode.com/problems/binary-number-with-alternating-bits/description/

class Solution(object):
    def hasAlternatingBits(self, n):
        last_bit = 0
        if n & 1 == 1:
            last_bit = 1
        n = n >> 1
        while n:
            if n & 1 == last_bit:
                return False
            last_bit = n & 1
            n = n >> 1
        return True
            
        