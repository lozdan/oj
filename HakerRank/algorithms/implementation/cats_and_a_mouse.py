# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Cats and a Mouse
# problem url: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

for i in range(int(input())):
    x, y, z = list(map(int, input().split()))
    if abs(x - z) < abs(y - z):
        print("Cat A")
    elif abs(x - z) > abs(y - z):
        print("Cat B")
    else:
        print("Mouse C")
    