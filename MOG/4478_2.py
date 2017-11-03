# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Pie Problem I
# problem url: http://matcomgrader.com/problem/4478/pie-problem-i/
# date: 5/20/2017

numbers = input().split()
for i in range(2):
    numbers[i] = int(numbers[i])

more_divisors = 0
digit = 0
def divisors(a):
    current_divisior = 1
    cant_divisors = 0
    while a >= current_divisior:
        if a % current_divisior == 0:
            cant_divisors += 1
        current_divisior += 1
    return cant_divisors

for num in range(numbers[0], numbers[1]+1):
    if divisors(num) > more_divisors:
        digit = num
        more_divisors = divisors(num)
print(digit)