# author: Daniel Lozano
# source: HAckerRank(https://www.hackerrank.com )
# problem name: Algorithms > Warmup > Diagonal Difference
# problem url: https://www.hackerrank.com/challenges/diagonal-difference/problem

n = int(input())
matrix = []

for i in range(n):
    matrix.append([int(i) for i in input().split()])

carry_sum_1 = 0
for i in range(n):
    carry_sum_1 = carry_sum_1 + matrix[i][i]

carry_sum_2 = 0
for i in range(n - 1, -1, -1):
    carry_sum_2 = carry_sum_2 + matrix[(n - 1) - i][i]

print(abs(carry_sum_1 - carry_sum_2))