# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Search > Missing Numbers
# problem url: https://www.hackerrank.com/challenges/missing-numbers/problem

n = int(input())
A = list(map(int, input().split()))
check_A = [0] * 10000

m = int(input())
B = list(map(int, input().split()))
check_B = [0] * 10000

for i in range(m):
    if i < n:
        check_A[A[i]] += 1
    check_B[B[i]] += 1

answer = []
for j in range(10000):
    if check_A[j] != 0 and check_B[j] != 0 and check_A[j] != check_B[j]:
        answer.append(j)
print(*sorted(answer))

