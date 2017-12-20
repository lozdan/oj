# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: Plus Minus
# problem url: https://www.hackerrank.com/challenges/plus-minus/problem
# date: 7/10/2017

n = int(input())
list = input().split()
for i in range(n):
    list[i] = int(list[i])

positives = []
negatives = []
zeros = []
for i in range(n):
    if list[i] > 0:
        positives.append(list[i])
    elif list[i] < 0:
        negatives.append((list[i]))
    else:
        zeros.append(list[i])
positives = len(positives) / n
negatives = len(negatives) / n
zeros = len(zeros) / n
print(str.format('{0:.6f}', positives))
print(str.format('{0:.6f}', negatives))
print(str.format('{0:.6f}', zeros))