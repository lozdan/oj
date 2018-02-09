# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Calculadora del tío de Fito
# problem url: http://matcomgrader.com/problem/5875/calculadora-del-tio-de-fito/	

first_number = int(input())
operator = input()
second_number = int(input())

if operator == "*":
    print(first_number * second_number)
else:
    print(first_number + second_number)
