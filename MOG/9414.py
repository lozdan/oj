# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Odd Or Even
# problem url: http://matcomgrader.com/problem/9414/odd-or-even/

while True:
    n = int(input())

    if n == 0:
        break

    mary = list(map(int, input().split()))
    john = list(map(int, input().split()))

    mo = sum(x & 1 for x in mary)
    jo= sum(x & 1 for x in john)

    print(n - (min(mo, n - jo) + min(n - mo, jo)))
