# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Implementation > Birthday Chocolate
# problem url: https://www.hackerrank.com/challenges/the-birthday-bar/problem

n = int(input())

chocolate_bar = list(map(int, input().split()))

d, m = list(map(int, input().split()))

answer = 0

for i in range(n):
    if i + m > len(chocolate_bar):
        break
    elif sum(chocolate_bar[i: i + m ]) == d:
        answer += 1
        
print(answer)
        