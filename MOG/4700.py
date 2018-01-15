# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Triangulos
# problem url: http://matcomgrader.com/problem/4700/triangulos/

numbers = []

while True:
    x = int(input())
    if x == 0:
        break
    numbers.append(x)

numbers = sorted(numbers)

for i in range(2, len(numbers)):
    if numbers[i - 2] + numbers[i - 1] > numbers[i]:
        print(numbers[i], numbers[i - 1], numbers[i - 2])
        exit()

print("NO")
