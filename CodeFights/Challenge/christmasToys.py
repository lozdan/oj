# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > christmasToys
# problem url: https://codefights.com/challenge/RHD48pZQdohiBQjLa

def christmasToys(toys):
    levels = [[0]]
    while levels[-1]:
        current_level = []
        for u in levels[-1]:
            current_level += toys[u]
        levels.append(current_level)
    return levels[:-1]
