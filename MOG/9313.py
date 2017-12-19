# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Football
# problem url: http://matcomgrader.com/problem/9313/football/

n, g = [int(i) for i in input().split()]

difference = []

for i in range(n):
    s, r = [int(i) for i in input().split()]
    difference.append(r - s)

difference = sorted(difference)

score = 0
for i in range(n):
    if difference[i] < 0:
        score += 3
    else:
        x = min(difference[i] + 1, g)
        if x == difference[i]:
            score += 1
        elif x > difference[i]:
            score += 3
        g -= x

print(score)