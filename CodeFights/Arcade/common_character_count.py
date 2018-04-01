# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: commonCharacterCount
# problem url: https://codefights.com/arcade/intro/level-3/JKKuHJknZNj4YGL32/description

def commonCharacterCount(s1, s2):
    alphabet = [0] * 26
    total = 0
    
    for char in s1:
        alphabet[ord(char) - 97] += 1
    
    for char1 in s2 :
        if alphabet[ord(char1) - 97] > 0:
            total += 1
            alphabet[ord(char1) - 97] -= 1
            
    return total
    
