# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Contests > Summer Lesson
# problem url: https://www.hackerrank.com/contests/university-codesprint-4/challenges/summer-lesson/problem

n, m = list(map(int, input().split()))
students = map(int, input().split())

classes = [0] * m
for stud in students:
    classes[stud] += 1
print(*classes)
