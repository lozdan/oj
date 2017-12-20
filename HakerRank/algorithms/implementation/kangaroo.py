# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Kangaroo
# problem url: https://www.hackerrank.com/challenges/kangaroo/problem
# date: 8/10/2017

x1, v1, x2, v2 = [int(x) for x in input().split()]

if v1 > v2:
    while x1 < x2:
        x1 += v1
        x2 += v2
        if x1 == x2:
            print("YES")
            exit()
    print("NO")
else:
    print("NO")