# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > is_palindrome
# problem url: https://codefights.com/challenge/3ucwTksArfYnhXddD

def is_palindrome(n):
    return int(str(n) == str(n)[::-1])