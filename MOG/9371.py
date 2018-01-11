# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Flowers Flourish from France
# problem url: http://matcomgrader.com/problem/9371/flowers-flourish-from-france/

while True:
    x = list(map(list, input().split()))
    if x == [["*"]]:
        break
    else:
        ans = "Y"
        for i in range(1, len(x)):
            if x[i][0].lower() != x[i - 1][0].lower():
                ans = "N"
                break
        print(ans)

