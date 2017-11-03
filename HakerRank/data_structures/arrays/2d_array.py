# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Arrays: 2D Array - DS
# problem url: https://www.hackerrank.com/challenges/2d-array/problem
# date: 8/16/2017

array = []
for i in range(6):
    array.append(input().split())
    for j in range(6):
        array[i][j] = int(array[i][j])

higher = -999999999
for i in range(4):
    for j in range(4):
        add = array[i][j] + array[i][j+1] + array[i][j+2] + array[i+1][j+1] + array[i+2][j] + array[i+2][j+1] + array[i+2][j+2]
        if add > higher:
            higher = add

print(higher)