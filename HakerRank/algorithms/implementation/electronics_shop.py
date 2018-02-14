# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Electronics Shop
# problem url: https://www.hackerrank.com/challenges/electronics-shop/problem

s, n, m = list(map(int, input().split()))
keyboard = list(map(int, input().split()))
mouse = list(map(int, input().split()))

ans = -1

for k in keyboard:
    for mo in mouse:
        if s >= k + mo > ans:
            ans = k + mo
print(ans)
