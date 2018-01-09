# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Bingo!
# problem url: http://matcomgrader.com/problem/9367/bingo/

while True:
    n, b = map(int, input().split())
    if n == 0 and b == 0:
        break
    numbers = list(map(int, input().split()))
    check = [0] * (n + 1)
    count = n + 1
    for i in range(b):
        if check[numbers[i]] == 0:
            check[numbers[i]] = 1
            count -= 1
        for j in range(i + 1, b):
            difference = abs(numbers[i] - numbers[j])
            if check[difference] == 0:
                check[difference] = 1
                count -= 1
    if count > 0:
        print("N")
    else:
        print("Y")
