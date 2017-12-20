# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: Birthday Cake Candles
# problem url: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# date: 7/10/2017

n = int(input())
heights = input().split()
for i in range(n):
    heights[i] = int(heights[i])

heights.sort()
candles = 0
for i in range(n):
    if heights[n-1-i] == heights[-1]:
        candles +=1
print(candles)