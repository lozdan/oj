# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Sorting: Counting Sort 2
# problem url: https://www.hackerrank.com/challenges/countingsort2/problem
# date: 8/20/2017

n = int(input())
array = [int(i) for i in input().split()]

count = [0 for i in range(max(array)+1)]
for x in array:
    count[x] +=1

output = []
for i in range(max(array)+1):
    if count[i] == 1:
        output.append(i)
    elif count[i] > 1:
        for j in range(count[i]):
            output.append(i)

print(*output)