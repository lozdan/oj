# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Arrays: Dynamic Array
# problem url: https://www.hackerrank.com/challenges/dynamic-array/problem
# date: 8/17/2017

n_q = [int(i) for i in input().split()]
cases = []
for i in range(n_q[1]):
    cases.append([int(j) for j in input().split()])
seq_list = []
for i in range(n_q[0]):
    seq_list.append([])
last_answer = 0


for i in range(n_q[1]):
    index = (cases[i][1] ^ last_answer) % n_q[0]
    if cases[i][0] == 1:
        seq_list[index].append(cases[i][2])
    else:
        last_answer = seq_list[index][cases[i][2] % len(seq_list[index])]
        print(last_answer)