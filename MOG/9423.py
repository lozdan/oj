# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Where Are My Genes
# problem url: http://matcomgrader.com/problem/9423/where-are-my-genes/

case_number = 1

while True:
    n = int(input())

    if n == 0:
        break

    genes = list(range(1, n + 1))

    reversals = []
    queries = []

    for i in range(int(input())):
        x = list(map(int, input().split()))
        x[0] -= 1
        x[1] -= 1
        reversals.append(x)

    for j in range(int(input())):
        queries.append(int(input()))

    print("Genome {}".format(case_number))

    for num in queries:
        ind = genes.index(num)
        for rev in reversals:
            if rev[0] <= ind <= rev[1]:
                ind = rev[1] - (ind - rev[0])
        print(ind + 1)
    case_number += 1
