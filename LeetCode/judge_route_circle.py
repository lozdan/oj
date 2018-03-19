# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Judge Route Circle
# problem url: https://leetcode.com/problems/judge-route-circle/description/

class Solution(object):
    def judgeCircle(self, moves):
        x = 0
        y = 0
        for lett in moves:
            if lett == "U":
                y += 1
            elif lett == "D":
                y -= 1
            elif lett == "L":
                x += 1
            else:
                x -= 1
        if x or y:
            return False
        return True
