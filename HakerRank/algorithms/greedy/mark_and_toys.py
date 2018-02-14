# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Greedy > Mark and Toys
# problem url: https://www.hackerrank.com/challenges/mark-and-toys/problem

n, k = list(map(int, input().split()))

toys = sorted(list(map(int, input().split())))

answer = 0
for toy in toys:
    if k - toy >= 0:
        answer += 1
        k -= toy
print(answer)
