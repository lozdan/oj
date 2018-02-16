# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Jumping on the Clouds: Revisited
# problem url: https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

n, k = list(map(int, input().split()))
clouds = list(map(int, input().split()))

start = clouds[0]
clouds[0] = 2
count = k % n
energy = 100
while clouds[count] != 2:
    if clouds[count] == 1:
        energy -= 2
    energy -= 1
    count = (count + k) % n
if start == 0:
    print(energy - 1)
else:
    print(energy - 3)
	