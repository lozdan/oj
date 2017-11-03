# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Algorithms: Implementation: Grading Students
# problem url: https://www.hackerrank.com/challenges/grading/problem
# date: 8/10/2017

for i in range(int(input())):
    grade = int(input())
    if grade >= 38:
        for x in range(1,3):
            if (grade + x) % 5 == 0:
                grade = grade + x
                break
    print(grade)