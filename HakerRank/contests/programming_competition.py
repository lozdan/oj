# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Contests > Programming Competition
# problem url: https://www.hackerrank.com/contests/hackerrank-hiring-contest/challenges/programming-competition/problem

answer = []
for i in range(int(input())):
    name, d, j = input().split()
    d, j = int(d), int(j)
    if not answer or answer[1] < j - d:
        answer = [name, j - d]

print(*answer)
    