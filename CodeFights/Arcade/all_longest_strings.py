# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: All Longest Strings
# problem url: https://codefights.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL/description

def allLongestStrings(inputArray):
    max_lenght = 0
    answer = []
    for c in inputArray:
        if len(c) > max_lenght:
            max_lenght = len(c)
    
    for m in inputArray:
        if len(m) == max_lenght:
            answer.append(m)
            
    return answer
