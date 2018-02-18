# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Roman to Integer
# problem url: https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s):
        translate = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        num = 0
        for i in range(len(s) - 1):
            if translate[s[i]] >= translate[s[i + 1]]:
                num += translate[s[i]]
            else:
                num -= translate[s[i]]
        return num + translate[s[-1]]
