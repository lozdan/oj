# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Partición en parejas
# problem url: http://matcomgrader.com/problem/9244/particion-en-parejas/
# date: 9/23/2017

n = int(input())
couples = [int(i) for i in input().split()]

couples.sort()
max_value = 0

count = 0
while count < n:
    max_value += abs(couples[count] - couples[-1])
    del couples[-1]
    count += 1

print(max_value)