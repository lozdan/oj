# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Se puede o NO se Puede
# problem url: http://matcomgrader.com/problem/143/se-puede-o-no-se-puede/
# date: 5/18/2017

n = int(input())
for i in range(n):
    line = input().split()
    for j in range(3):
        line[j] = int(line[j])
    line.sort()
    if line[-1] < line[0] + line[1]:
        print("YES")
    else:
        print("NO")