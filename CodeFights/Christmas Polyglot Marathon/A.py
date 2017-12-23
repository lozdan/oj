# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: bottlesOfSoda
# problem url: https://codefights.com/tournaments/a2ccKEqrGXWGebLva/A

def bottlesOfSoda(n, m, k):
    drinked = 0
    while n != 0 or m >= k:        
        m += n
        drinked += n
        n = 0
        if k <= m:
            n = m // k
            m = m % k
    return drinked