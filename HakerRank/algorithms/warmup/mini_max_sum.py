# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Warmup: Mini-Max Sum
# problem url: https://www.hackerrank.com/challenges/mini-max-sum/problem
# date: 7/10/2017

list = input().split()
for i in range(5):
    list[i] = int(list[i])
k = []
for i in range(5):
    a = list.pop(i)
    b = sum(list)
    k.append(b)
    list.insert(i,a)
print(min(k), max(k))