# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Sorting: Running Time of Algorithms
# problem url: https://www.hackerrank.com/challenges/runningtime/problem
# date: 8/15/2017

n = int(input())
array = [int(i) for i in input().split()]

steps = 0
for i in range(1, n):
    count = i
    while count > 0 and array[count] < array[count-1]:
        array[count], array[count-1] = array[count-1], array[count]
        count -= 1
        steps += 1
print(steps)