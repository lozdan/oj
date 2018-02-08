# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Generando cadena homogénea
# problem url: http://matcomgrader.com/problem/8080/generando-cadena-homogenea/

string = input()
a_changes = 0
b_changes = 0

count = 0
while count < len(string):
    if string[count] == 'a':
        while count < len(string) and string[count] == 'a':
            count += 1
        a_changes += 1
    elif string[count] == 'b':
        while count < len(string) and string[count] == 'b':
            count += 1
        b_changes += 1

print(min(a_changes, b_changes))

