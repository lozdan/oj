# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Implementation > Circular Array Rotation
# problem url: https://www.hackerrank.com/challenges/circular-array-rotation/problem

n, k, q = list(map(int, input().split()))
numbers = list(map(int, input().split()))

for i in range(k):
    numbers.insert(0,numbers.pop())
    
for i in range(q):
    print(numbers[int(input())])
