# author: Daniel Lozano
# source: CodeWars ( http://www.codewars.com )
# problem name: Kata > Alphabetically ordered
# problem url: https://www.codewars.com/kata/alphabetically-ordered

def alphabetic(s):
    for i in range(1, len(s)):
        if ord(s[i - 1]) > ord(s[i]):
            return False
    return True
    