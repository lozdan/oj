# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Algorithms > Implementation > Bon Appétit
# problem url: https://www.hackerrank.com/challenges/bon-appetit/problem

n, k = list(map(int, input().split()))

bill = list(map(int, input().split()))

b = int(input())

anna_share = (sum(bill) - bill[k]) // 2

if anna_share == b:
    print("Bon Appetit")
else:
    print(b - anna_share)

