# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Stacks: Game of Two Stacks
# problem url: https://www.hackerrank.com/challenges/game-of-two-stacks/problem
# date: 9/10/2017

for i in range(int(input())):
    n, m, x = [int(i) for i in input().split()]

    a = [0] + [int(i) for i in input().split()]
    b = [0] + [int(i) for i in input().split()]

    score = 0

    for i in range(1, n + 1):
        a[i] = a[i] + a[i - 1]

    for i in range(1, m + 1):
        b[i] = b[i] + b[i - 1]

    g = 0
    while g <= m and a[0] + b[g] <= x:
        g += 1
    g -= 1

    for k in range(n + 1):
        while g >= 0:
            if a[k] + b[g] <= x:
                score = max(g + k, score)
                break
            else:
                g -= 1
    print(score)