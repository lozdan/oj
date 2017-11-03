# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: A ordenar!
# problem url: http://matcomgrader.com/problem/8084/a-ordenar/
# date: 5/6/2017

n = int(input())
line = input().split()

line.sort(key=int)
print(" ".join(line))