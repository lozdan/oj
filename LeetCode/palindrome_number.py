# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Palindrome Number
# problem url: https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1]
        
        