# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Weekend Lottery
# problem url: http://matcomgrader.com/problem/9409/weekend-lottery/

while True:
    n, c, k = list(map(int, input().split()))

    if n == c == k == 0:
        break

    check = [0] * k

    for i in range(n):
        line = list(map(int, input().split()))
        for c in line:
            check[c - 1] += 1

    min_value = min(check)

    for j in range(k):
        if check[j] == min_value:
            print(j + 1, end=" ")
    print(end='\n')
