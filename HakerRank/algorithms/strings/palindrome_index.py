# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Strings > Palindrome Index
# problem url: https://www.hackerrank.com/challenges/palindrome-index/problem

def solution(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - (i + 1)]:
            word = word[:i] + word[i + 1:]
            if word == word[::-1]:
                return i
            else:
                return length - (i + 1)
    return -1


for _ in range(int(input())):
    word = input()
    print(solution(word))


