# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Apple and Orange
# problem url: https://www.hackerrank.com/challenges/apple-and-orange/problem
# date: 8/10/2017

s, t = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]
m, n = [int(x) for x in input().split()]
distance_app = [int(x) for x in input().split()]
distance_oran = [int(x) for x in input().split()]

apples = 0
for i in range(m):
    if distance_app[i] >= s - a and distance_app[i] <= t - a:
        apples += 1
        
oranges = 0
for i in range(n):
    if distance_oran[i] <= t - b and distance_oran[i] >= s - b:
        oranges += 1
        
print(apples)
print(oranges)