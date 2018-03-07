# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Strings > Strong Password
# problem url: https://www.hackerrank.com/challenges/strong-password/problem

n = int(input())
password = input()

specials_char = {"!", "@", "#", "$", "%", "^",
                 "&", "*", "(", ")", "-", "+"}
accept = 0
upper = False
lower = False
char = False
number = False
i = 0
while i < n and accept < 4:
    if not upper and 90 >= ord(password[i]) >= 65:
        upper = True
        accept += 1
    elif not lower and 122 >= ord(password[i]) >= 97:
        lower = True
        accept += 1
    elif not char and password[i] in specials_char:
        char = True
        accept += 1
    elif not number and password[i].isdigit():
        number = True
        accept += 1
    i += 1

if n >= 6:
    print(4 - accept)
else:
    if 6 - n >= 4 - accept:
        print(6 - n)
    else:
        print(4 - accept)
