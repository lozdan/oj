# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > Is_Anagram
# problem url: https://codefights.com/challenge/hyp82rYXic9RKR2kj

def Is_Anagram(S, T):
    operations = 0
    T = list(T)
    for c in S:
        if c in T:
            T.remove(c)
        else:
            operations += 1            
    return operations
