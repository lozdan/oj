# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Fito Task
# problem url: http://matcomgrader.com/problem/27/fito-task
# date: 5/28/2017

numbers = input().split()
number_1 = [int(i) for i in str(numbers[0])]
number_2 = [int(i) for i in str(numbers[1])]
for j in range(len(number_1)):
    if number_1[j] == 6:
        number_1[j] = 5
    if number_2[j] == 6:
        number_2[j] = 5
lower_number = int("".join(map(str,number_1))) + int("".join(map(str,number_2)))

for k in range(len(number_1)):
    if number_1[k] == 5:
        number_1[k] = 6
    if number_2[k] == 5:
        number_2[k] = 6
higher_number = int("".join(map(str, number_1))) + int("".join(map(str, number_2)))

print(lower_number, higher_number)