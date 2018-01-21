# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Implementation > Utopian Tree
# problem url: https://www.hackerrank.com/challenges/utopian-tree/problem

for i in range(int(input())):
    cycle = int(input())
    height = 1
    for j in range(cycle):
        if j % 2 == 0:
            height *= 2
        else:
            height += 1
    print(height)
    