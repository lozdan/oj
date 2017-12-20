# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Sorting: Correctness and the Loop Invariant
# problem url: https://www.hackerrank.com/challenges/correctness-invariant/problem
# date: 8/15/2017

def insertion_sort(l):
    for i in range(1, len(l)):
        count = i
        while count > 0 and l[count] < l[count-1]:
            l[count], l[count - 1] = l[count - 1], l[count]
            count -= 1


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))