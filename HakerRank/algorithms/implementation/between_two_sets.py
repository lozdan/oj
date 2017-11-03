# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Between Two Sets
# problem url: https://www.hackerrank.com/challenges/between-two-sets/problem
# date: 8/10/2017

n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

count = 0
x = a[0] - 1
while x <= b[0]:
    x += 1
    for i in range(n):
        if x % a[i] != 0:
            break
        if i == n -1 and x % a[i] == 0:
            for j in range(m):
                if b[j] % x != 0:
                    break
                if j == m - 1 and b[j] % x == 0:
                    count += 1
print(count)