# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Contests > Acid Naming
# problem url: https://www.hackerrank.com/contests/w36/challenges/acid-naming/problem

n = int(input())

for i in range(n):
    string = input()
    if len(string) > 6 and string[:5] == "hydro" and string[-2:] == "ic":
        print("non-metal acid")
    elif string[-2:] == "ic":
        print("polyatomic acid")
    else:
        print("not an acid")
