# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: sumOfTwo
# problem url: https://codefights.com/interview-practice/task/Hm98RnqK9Be575yoj
# date: 8/15/2017

def sumOfTwo(a, b, v):
    a.sort()
    b.sort()
    b = set(b)
    for i in range(len(a)):
        if v - a[i] in b:
            return True
    return False