# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Implementation > Climbing the Leaderboard
# problem url: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

n = int(input())
leaderboard = list(map(int, input().split()))
leaderboard[0] = 1, leaderboard[0]

for i in range(1, n):
    if leaderboard[i] == leaderboard[i - 1][1]:
        leaderboard[i] = leaderboard[i - 1][0], leaderboard[i]
    else:
        leaderboard[i] = leaderboard[i - 1][0] + 1, leaderboard[i]

k = int(input())
alice = list(map(int, input().split()))
alice_position = leaderboard[-1][0] + 1

count = n - 1

for j in range(k):
    while alice[j] >= leaderboard[count][1] and alice_position != 1:
        alice_position = leaderboard[count][0]

        count -= 1
    print(alice_position)
