# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Grandpa is Famous
# problem url: http://matcomgrader.com/problem/9433/grandpa-is-famous/

while True:
    n, m = list(map(int, input().split()))

    if n == 0 and m == 0:
        break

    check = [0] * 10000

    max_value = 0
    for i in range(n):
        for position in list(map(int, input().split())):
            check[position] += 1
            if check[position] > max_value:
                max_value = check[position]

    second_place = []
    act_sec = 0
    for j in range(len(check)):
        if check[j] < max_value and act_sec < check[j]:
            second_place = [j]
            act_sec = check[j]
        elif check[j] < max_value and check[j] == act_sec:
            second_place.append(j)

    print(*second_place)

