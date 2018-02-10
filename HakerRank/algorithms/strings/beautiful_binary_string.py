# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Strings > Beautiful Binary String
# problem url: https://www.hackerrank.com/challenges/beautiful-binary-string/problem

n = int(input())
string = list(input())

changes = 0
for i in range(n - 2):
    if string[i:i + 3] == ['0', '1', '0']:
        string[i + 2] = '1'
        changes += 1

print(changes)
