# author: Daniel Lozano
# source: MatcomOnlineGrader (MOG) ( http://matcomgrader.com )
# problem name: Another Brick in the Wall
# problem url: http://matcomgrader.com/problem/9229/another-brick-in-the-wall/
# date: 9/17/2017

n = int(input())

printers = 1
days_old = 1000000
count = 0
days_news = 0

while True:
    statues = 0
    while statues < n:
        statues += printers
        days_news += 1
    count += 1
    if days_news > days_old:
        break
    printers = printers * 2
    days_old = days_news
    days_news = count

print(days_old)