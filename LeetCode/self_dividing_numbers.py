# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Self Dividing Numbers
# problem url: https://leetcode.com/problems/self-dividing-numbers/description/

class Solution(object):
    def selfDividingNumbers(self, left, right):
        answer = []
        for num in range(left, right + 1):
            if self.div(num):
                answer.append(num)
        return answer
            
    def div(self, num):
        n = num
        while n:
            if n % 10 == 0 or num % (n %10) != 0:
                return False
            n = n // 10
        return True
        