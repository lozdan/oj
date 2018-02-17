# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Contests > Exam Rush
# problem url: https://www.hackerrank.com/contests/rookierank-4/challenges/exam-rush/problem

n, t = list(map(int, input().split()))

chapters = []

for i in range(n):
    chapters.append(int(input()))

chapters = sorted(chapters)
take_time = 0
count = 0
read_chapters = 0

while chapters[count] + take_time <= t:
    take_time += chapters[count]
    read_chapters += 1
    count += 1

print(read_chapters)
