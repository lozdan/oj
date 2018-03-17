# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Rotate String
# problem url: https://leetcode.com/problems/rotate-string/description/

class Solution:
    def rotateString(self, A, B):
        count = 0
        while A != B and count < len(A):
            A = A[1:] + A[0]
            count += 1
        if A == B:
            return True
        return False
        