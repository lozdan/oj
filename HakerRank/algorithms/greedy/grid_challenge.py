# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Greedy > Grid Challenge
# problem url: https://www.hackerrank.com/challenges/grid-challenge/problem

def sort_grid(grid, k):
    for l in range(k - 1):
        for m in range(k):
            if grid[l][m] > grid[l + 1][m]:
                return "NO"
    return "YES"


for i in range(int(input())):
    k = int(input())
    grid = []
    for j in range(k):
        grid.append(sorted(input()))
    print(sort_grid(grid, k))

