# author: Daniel Lozano
# source: HackerRank(https://www.hackerrank.com )
# problem name: Algorithms > Strings > Two Strings
# problem url: https://www.hackerrank.com/challenges/two-strings/problem

def check_sub_str(w_1, w_2):
    for lett in w_1:
        if lett in w_2:
            return True
    return False

for i in range(int(input())):
    word_1 = input()
    word_2 = set(input())
    if check_sub_str(word_1, word_2):
        print("YES")
    else:
        print("NO")

    