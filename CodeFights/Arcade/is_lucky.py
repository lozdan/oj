# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: isLucky
# problem url: https://codefights.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ/description

def isLucky(n):
    n = list(map(int, str(n)))
    return sum(n[:len(n) // 2]) == sum(n[len(n) // 2:])
