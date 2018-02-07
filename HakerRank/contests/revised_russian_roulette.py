# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Contests > Revised Russian Roulette
# problem url: https://www.hackerrank.com/contests/w36/challenges/revised-russian-roulette

n = int(input())

doors = input().split()
max_oper = 0
min_oper = 0

i = 0
while i < n:
    if doors[i] == '1':
        min_oper += 1
        max_oper += 1
        if i < n - 1 and doors[i + 1] == '1':
            max_oper += 1
            i += 2
            continue
    i += 1

print(min_oper, max_oper)
