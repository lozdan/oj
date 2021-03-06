# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Sorting: Insertion Sort - Part 2
# problem url: https://www.hackerrank.com/challenges/insertionsort2/problem
# date: 8/15/2017

n = int(input())
array = [int(i) for i in input().split()]


for i in range(1, n):
    count = i
    while count > 0 and array[count] < array[count-1]:
        array[count], array[count - 1] = array[count - 1], array[count]
        count -= 1
    print(*array)