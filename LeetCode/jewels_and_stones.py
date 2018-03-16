# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Jewels and Stones
# problem url:https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, J, S):
        count = 0 
        for lett in J:
            for c in S:
                if lett == c:
                    count += 1
        return count
        