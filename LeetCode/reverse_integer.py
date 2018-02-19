# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Reverse Integer
# problem url: https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x):
        if x > 0:
            answer = self.reverse_1(x)
            if answer <= 2 ** 31 - 1:
                return answer
            return 0
        else:
            answer = self.reverse_1(-x) * -1
            if answer >= -2 ** 31:
                return answer
            return 0

    def reverse_1(self, x):
        y = 0
        while x != 0:
            y = y * 10
            y = y + (x % 10)
            x = x // 10
        return y