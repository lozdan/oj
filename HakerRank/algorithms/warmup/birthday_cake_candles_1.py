# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: Birthday Cake Candles
# problem url: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# date: 7/10/2017

n = int(input())
heights = input().split()
for i in range(n):
    heights[i] = int(heights[i])

candles = 0
heigh = max(heights)
for i in range(n):
    if heigh == heights[i]:
        candles +=1
print(candles)