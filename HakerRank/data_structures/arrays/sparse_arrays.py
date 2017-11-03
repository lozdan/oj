# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Arrays: Sparse Arrays
# problem url: https://www.hackerrank.com/challenges/sparse-arrays/problem
# date: 8/23/2017

n = int(input())
arr_1 = []
for i in range(n):
    arr_1.append(input())

n_2 = int(input())
arr_2 = []
for i in range(n_2):
    arr_2.append(input())


for i in range(n_2):
    count = 0
    for j in range(n):
        if len(arr_1[j]) == len(arr_2[i]):
            for k in range(len(arr_2[i])):
                if arr_1[j][k] != arr_2 [i][k]:
                    break
            else:
                count += 1
    print(count)