# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Counting Valleys
# problem url: https://www.hackerrank.com/challenges/counting-valleys/problem

n = int(input())

hike = input()

sea_level = 0
valley = 0

for step in hike:
    if step == "U":
        sea_level += 1
        if sea_level == 0:
            valley += 1
    else:
        sea_level -= 1
        
print(valley)
    