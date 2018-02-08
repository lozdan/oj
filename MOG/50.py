# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: El Numero Decodificado
# problem url: http://matcomgrader.com/problem/50/el-numero-decodificado/

n = int(input())

count = 1


def digits_sum(num):
    add = 0
    while num != 0:
        add += num % 10
        num = num // 10
    return add


while count != digits_sum(n - count):
    count += 1

print(n - count)
