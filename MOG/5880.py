# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: A clasificar Triángulos
# problem url: http://matcomgrader.com/problem/5880/a-clasificar-triangulos/
# date: 5/10/2017

n = int(input())
for i in range(n):
    line = input().split()
    for j in range(3):
        line[j] = int(line[j])
    line.sort()
    if line[0] + line[1] <= line[2]:
        print("Case #{}: invalid!".format(i +1))
    elif line[0] == line[1] and line[1] == line[2]:
        print("Case #{}: {}".format(i + 1, "equilateral"))
    elif line[0] != line[1] and line[1] != line[2] and line[2] != line[0]:
        print("Case #{}: {}".format(i + 1, "scalene"))
    elif line[0] == line[1] or line[0] == line[2] or line[1] == line[2]:
        print("Case #{}: {}".format(i + 1, "isosceles"))