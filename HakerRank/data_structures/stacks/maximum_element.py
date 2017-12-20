# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Stacks: Maximum Element
# problem url: https://www.hackerrank.com/challenges/maximum-element/problem
# date: 9/9/2017

n = int(input())
arr = []
for i in range(n):
    arr.append(input().split())
    for j in range(len(arr[i])):
        arr[i][j] = int(arr[i][j])

stack = []
higher = [0]
    
for i in range(n):
    if arr[i][0] == 1:
        stack.append(arr[i][1])
        if arr[i][1] >= higher[-1]:
            higher.append(arr[i][1])
    elif arr[i][0] == 2:
        if stack[-1] == higher[-1]:
            del higher[-1]
        del stack[-1]
    elif arr[i][0] == 3:
        print(higher[-1])