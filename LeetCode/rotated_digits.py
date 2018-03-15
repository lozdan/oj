# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Rotated Digits
# problem url: https://leetcode.com/problems/rotated-digits/description/

class Solution:
    def rotatedDigits(self, N):
        good_nums = 0
        for i in range(1, N + 1):
            if self.digits(i):
                good_nums += 1
        return good_nums
                
    def digits(self, num):
        rotate_nums = {2, 5, 6, 9}
        invalid_nums = {3, 4, 7}
        answer = False
        while num:
            if num % 10 in invalid_nums:
                return False
            elif num % 10 in rotate_nums:
                answer = True
            num = num // 10
        return answer
        
        