# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Keyboard Row
# problem url: https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words):
        keyboard = [{"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}, {"a", "s", "d", "f", "g", "h", "j", "k", "l"},
                    {"z", "x", "c", "v", "b", "n", "m"}]
        answer = []
        for word in words:
            word1 = word.lower()
            if word1[0] in keyboard[0]:
                if self.check_row(word1, keyboard[0]):
                    answer.append(word)
            elif word1[0] in keyboard[1]:
                if self.check_row(word1, keyboard[1]):
                    answer.append(word)
            else:
                if self.check_row(word1, keyboard[2]):
                    answer.append(word)
                
        return answer    

    def check_row(self, word, row):
        for lett in word:
            if lett not in row:
                return False
        return True
