# author: Daniel Lozano
# source: HackerRank(https://www.hackerrank.com )
# problem name: Algorithms > Strings > CamelCase
# problem url: https://www.hackerrank.com/challenges/camelcase/problem

s = input().strip()

words = 1
for i in range(len(s)):
    if s[i] == s[i].upper():
        words += 1
print(words)