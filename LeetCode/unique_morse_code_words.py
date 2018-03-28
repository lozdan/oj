# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Contest > Unique Morse Code Words
# problem url: https://leetcode.com/contest/weekly-contest-77/problems/unique-morse-code-words/

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        transformation = set()
        temp = ""
        
        for c in words:
            for i in range(len(c)):
                temp += morse[ord(c[i]) - 97]

            transformation.add(temp)
            temp = ""
            
        return len(transformation)
