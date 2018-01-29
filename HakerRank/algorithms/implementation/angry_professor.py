# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Implementation > Angry Professor
# problem url: https://www.hackerrank.com/challenges/angry-professor/problem

for i in range(int(input())):
    n, k = list(map(int, input().split()))
    students = list(map(int, input().split()))
    
    on_time = 0
    for c in students:
        if c <= 0:
            on_time += 1
    if on_time >= k:
        print("NO")
    else:
        print("YES")
    