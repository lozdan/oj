# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Tu viaje está aquí
# problem url: http://matcomgrader.com/problem/142/tu-viaje-esta-aqui/
# date: 6/4/2017

number_1 = input()
number_2 = input()
line_1 = []
line_2 = []
for x in number_1:
    line_1.append(ord(x) - (ord("A") - 1))
for x in number_2:
    line_2.append(ord(x) - (ord("A") - 1))

mult_1 = 1
for i in range(len(line_1)):
    mult_1 *= line_1[i]
mult_2 = 1
for i in range(len(line_2)):
    mult_2 *= line_2[i]

if mult_1 % 47 == mult_2 % 47:
    print("GO")
else:
    print("STAY")