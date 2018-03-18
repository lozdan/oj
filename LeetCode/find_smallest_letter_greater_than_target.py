# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Find Smallest Letter Greater Than Target
# problem url: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

class Solution:
    def nextGreatestLetter(self, letters, target):
        answer = []
        for lett in letters:
            if lett > target:
                answer.append(lett)
        if answer:
            return min(answer)
        return min(letters)
        