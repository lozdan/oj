# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Elementos consecutivos
# problem url: http://matcomgrader.com/problem/254/elementos-consecutivos/

n = int(input())
array = sorted(list(map(int, input().split())))

answer = 1
count = 0
m = set()
for c in array:
    if m and c - 1 not in m:
        if len(m) > answer:
            answer = len(m)
        m = set()
        m.add(c)
    else:
        m.add(c)

if answer > len(m):
    print(answer)
else:
    print(len(m))
