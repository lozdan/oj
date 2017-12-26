# author: Daniel Lozano
# source: CodeFights ( https://codefights.com )
# problem name: Challenge > timeDegrees
# problem url: https://codefights.com/challenge/BMAqHPYhhPdHTd7pz

def timeDegrees(t):
    h, m, s = [ int(i) for i in t.replace(":", " ").split()]
    if h > 12:
        h = h - 12
    h_position = (h + ((m * 60 + s) / 3600)) / 12
    s_position = s / 60
    distance = abs(h_position - s_position) 
    return int(360 * min(distance, 1 - distance))
