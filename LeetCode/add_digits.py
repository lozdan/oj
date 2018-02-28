# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Add Digits
# problem url: https://leetcode.com/problems/add-digits/description/

class Solution:
    def addDigits(self, num):
        while num > 9:
            num = self.adding(num)
        return num
            
    def adding(self, x):
        y = 0
        while x:
            y += x % 10
            x = x // 10
        return y
        