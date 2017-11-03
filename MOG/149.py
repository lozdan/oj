# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: La novia de Fito
# problem url: http://matcomgrader.com/problem/149/la-novia-de-fito/
# date: 5/6/2017

message = input()
count = 0
while count < len(message)-2:
    if message[count] == "a" and message[count+1] == "n" and message[count+2] == "a":
        message = message[:count] + message[count+3:]
        count -= 1
    else:
        count += 1
print(message)