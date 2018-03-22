# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Fizz Buzz
# problem url: https://leetcode.com/problems/fizz-buzz/description/

class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append("{}".format(i))
        return answer
        