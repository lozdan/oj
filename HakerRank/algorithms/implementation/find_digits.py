# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Implementation > Find Digits
# problem url: https://www.hackerrank.com/challenges/find-digits/problem

for i in range(int(input())):
    str_num = input()
    num = int(str_num)
    total = 0
    for dig in str_num:
        if dig != "0" and num % int(dig) == 0:
            total += 1
    print(total)
    