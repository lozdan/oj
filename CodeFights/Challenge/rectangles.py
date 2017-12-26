# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > rectangles
# problem url: https://codefights.com/challenge/9on2fva2RCFRrTmdd

def rectangles(n, m):
    return m * (m - 1) * n * (n - 1) // 4
