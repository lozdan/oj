# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Implementation > Day of the Programmer
# problem url: https://www.hackerrank.com/challenges/day-of-the-programmer/problem

year = int(input())

if year == 1918:
    print("26.09.1918")
else:
    if (year < 1918 and year % 4 == 0) or (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("12.09.{}".format(year))
    else:
        print("13.09.{}".format(year))
        