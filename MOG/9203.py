# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Igualando Lista
# problem url: http://matcomgrader.com/problem/9203/igualando-lista/
# date: 5/10/2017

n = int(input())
line = input().split()
for i in range(n):
    line[i] = int(line[i])
line.sort()

middle_number = line[len(line)//2]
steps = 0
for i in range(n):
    while line[i] != middle_number:
        if line[i] < middle_number:
            a = middle_number - line[i]
            steps += a
            line[i] = middle_number
        elif line[i] > middle_number:
            b = line[i] - middle_number
            steps += b
            line[i] = middle_number
print(steps)