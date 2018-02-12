# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Greedy > Marc's Cakewalk
# problem url: https://www.hackerrank.com/challenges/marcs-cakewalk/problem

n = int(input())
cupcakes = sorted(list(map(int, input().split())), reverse=True)

x = 0
miles = 0

for i in range(n):
    miles = miles + (cupcakes[i] * (2 ** i))

print(miles)
