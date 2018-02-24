# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Longest Substring Without Repeating Characters
# problem url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s):
        check = set()
        length = 0
        for i in range(len(s)):
            count = i
            while count < len(s) and s[count] not in check:
                check.add(s[count])
                count += 1
            if len(check) > length:
                length = len(check)
            check = set()
        return length
        