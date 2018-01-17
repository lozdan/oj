# author : Daniel Lozano
# source : HackerRank ( https://www.hackerrank.com )
# name   : Data Structures > Heap > Find the Running Median
# url    : https://www.hackerrank.com/challenges/find-the-running-median/problem
#
# solution
# --------
# `max_heap` store the  first  half  of  the  sorted  stream
# and  `min_heap`  the  second  half.  The  goal  is to keep
# the two  heaps  balanced  over  time. If  the  stream  has
# an odd  length,  the  `min_heap`  will  have  one  element
# more  than   `max_heap`.  The  median  can  be  calculated
# as  the  minimum element  of  the second half (`min_heap`)
# if the length of the `min_heap` is grater than `max_heap`.
# If  both  heaps  have the  same  length  the stream has an
# even number  of  elements then  the  median  is  the  mean
# of the the  higher element  of the first half (`max_heap`)
# and  the lowest element fo the  second half  (`min_heap`).

import heapq

max_heap = []
min_heap = []

for i in range(int(input())):
    x = int(input())
    if not min_heap or x >= min_heap[0]:
        heapq.heappush(min_heap, +x)
    else:
        heapq.heappush(max_heap, -x)
    if len(max_heap) == len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(max_heap) + 2 == len(min_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    if len(min_heap) != len(max_heap):
        median = min_heap[0]
    else:
        median = (min_heap[0] - max_heap[0]) / 2
    print('%.1lf' % median)
