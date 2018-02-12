# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Greedy > Minimum Absolute Difference in an Array
# problem url: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

n = int(input())

numbers = sorted(list(map(int, input().split())), reverse=True)

answer = abs(numbers[0] - numbers[1])
count = 1
while count < n - 1:
    if abs(numbers[count] - numbers[count + 1]) <= answer:
        answer = abs(numbers[count] - numbers[count + 1])
    count += 1

print(answer)
