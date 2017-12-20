# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Strings > Funny String
# problem url: https://www.hackerrank.com/challenges/funny-string/problem

for _ in range(int(input())):
    s = list(map(ord, input()))
    funny, i = True, 1
    while i < len(s) and funny:
        if abs(s[i] - s[i - 1]) != abs(s[-i - 1] - s[-i]):
            funny = False
        i += 1    
    print("Funny" if funny else "Not Funny")
