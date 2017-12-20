# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Sorting: Intro to Tutorial Challenges
# problem url: https://www.hackerrank.com/challenges/tutorial-intro/problem
# date: 8/15/2017

value = int(input())
n = int(input())
array = input().split()
for i in range(n):
    array[i] = int(array[i])
    for j in range(n):
        if array[i] == value:
            print(i)
            break