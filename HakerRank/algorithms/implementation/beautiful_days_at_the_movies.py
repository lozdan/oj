# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Implementation > Beautiful Days at the Movies
# problem url: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

def reverse_number(num):
    reverse = 0
    while(num > 0):
        reminder = num %10
        reverse = (reverse * 10) + reminder
        num = num //10
    return reverse

i, j, k = list(map(int, input().split()))

total = 0

for c in range(i, j):
    if abs(c - reverse_number(c)) % k == 0:
        total += 1
print(total)
