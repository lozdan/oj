# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: Compare the Triplets
# problem url: https://www.hackerrank.com/challenges/compare-the-triplets/problem
# date: 7/10/2017


a = input().split()
b = input().split()
for i in range(3):
    a[i] = int(a[i])
    b[i] = int(b[i])

alice = 0
bob = 0
for i in range(3):
    if a[i] > b[i]:
        alice = alice + 1
    elif a[i] < b[i]:
        bob = bob + 1
print(alice, bob)