# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Fito y sus Matemáticos Favoritos
# problem url: http://matcomgrader.com/problem/5871/fito-y-sus-matematicos-favoritos/
# date: 5/13/2017

while True:
    line = input()
    if line == "0 0 0 0":
        break
    line = line.split()
    for i in range(4):
        line[i] = int(line[i])
    print("{} {}".format(line[2]-line[1], line[3]-line[0]))