# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Implement strStr()
# problem url: https://leetcode.com/problems/implement-strstr/description/

class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1