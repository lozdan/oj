# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Implementation > The Hurdle Race
# problem url: https://www.hackerrank.com/challenges/the-hurdle-race/problem

n, k = map(int, input().split())

numbers = map(int, input().split())

diff = max(numbers) - k 

if diff > -1:
    print(diff)
else:
    print(0)
