# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures > Heap > Jesse and Cookies
# problem url: https://www.hackerrank.com/challenges/jesse-and-cookies/problem

import heapq

n, k = map(int, input().split())
cookies = list(map(int, input().split()))

heapq.heapify(cookies)

steps = 0
while len(cookies) >= 2 and cookies[0] < k:
    a = heapq.heappop(cookies)
    b = heapq.heappop(cookies)
    heapq.heappush(cookies, a + 2 * b)
    steps += 1

if cookies[0] >= k:
    print(steps)
else:
    print(-1)

