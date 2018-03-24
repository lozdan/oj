# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Contests > Train Ticket
# problem url: https://www.hackerrank.com/contests/101hack53/challenges/train-ticket/problem

n = int(input())

seats = ["SUB", "LB", "MB", "UB", "LB", "MB", "UB", "SLB"]

print(seats[n % 8])
