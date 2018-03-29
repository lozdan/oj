# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Greedy > Luck Balance
# problem url: https://www.hackerrank.com/challenges/luck-balance/problem

n, k = list(map(int, input().split()))
lucky_balance = 0
imp_contests = []

for i in range(n):
    l, t = list(map(int, input().split()))
    if t == 0:
        lucky_balance += l
    else:
        imp_contests.append(l)

imp_contests = sorted(imp_contests, reverse=True)
for j in range(len(imp_contests)):
    if j < k:
        lucky_balance += imp_contests[j]
    else:
        lucky_balance -= imp_contests[j]

print(lucky_balance)

