# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Pie Problem I
# problem url: http://matcomgrader.com/problem/4478/pie-problem-i/
# date: 5/20/2017

numbers = input().split()
for i in range(2):
    numbers[i] = int(numbers[i])

size_array = []
digits =[]
for num in range(numbers[0], numbers[1]+1):
    digits.append(num)
    long_divisors = 0
    for j in range(1,num+1):
        if num % j == 0:
            long_divisors += 1
    size_array.append(long_divisors)

place_higer_value = size_array.index(max(size_array))
print(digits[place_higer_value])