# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Sorting: Insertion Sort - Part 1
# problem url: https://www.hackerrank.com/challenges/insertionsort1/problem
# date: 8/15/2017

n = int(input())
array = input().split()
for i in range(len(array)):
    array[i] = int(array[i])

for i in range(n-1):
    a = array[i + 1]
    if array[i] > array[i+1]:
        for j in range(i, -1, -1):
            if array[j] < a:
                array[j+1] = a
                print(*array)
                break
            elif array[j] == a+1:
                array[j+1] = array[j]
                print(*array)
                array[j] = a
                print(*array)
                break
            array[j+1] = array[j]
            print(*array)