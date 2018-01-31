# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Pascal Library
# problem url: http://matcomgrader.com/problem/9420/pascal-library/

def dinner_assist(n, d, check):
    for i in range(d):
        dinner = list(map(int, input().split()))
        for j in range(n):
            check[j] += dinner[j]
            if check[j] == d:
                return True
    return False

while True:
    n, d = list(map(int, input().split()))

    if n == 0 and d == 0:
        break

    check = [0] * n

    if dinner_assist(n, d, check):
        print("yes")
    else:
        print("no")
