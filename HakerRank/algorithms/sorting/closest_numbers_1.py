# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Sorting: Closest Numbers
# problem url: https://www.hackerrank.com/challenges/closest-numbers/problem
# date: 8/20/2017

n = int(input())
array = [int(i) for i in input().split()]

array = sorted(array)

final_lst = []
lowest = 9*(10**7)
for i in range(n - 1):
    x = array[i + 1] - array[i]
    if x < lowest:
        lowest = x
        final_lst = []
        final_lst.append(array[i])
        final_lst.append(array[i+1])
    elif x == lowest:
        final_lst.append(array[i])
        final_lst.append(array[i+1])

print(*final_lst)