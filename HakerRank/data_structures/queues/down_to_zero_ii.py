# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Queues: Down to Zero II
# problem url: https://www.hackerrank.com/challenges/down-to-zero-ii/problem
# date: 9/12/2017

class Queue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._first_element = 0

    def enqueue(self, value):
        self._queue.append(value)
        self._count += 1

    def dequeue(self):
        if self._count > 0:
            self._first_element += 1
            self._count -= 1
        else:
            while True:
                pass
            raise Exception("Empty array")

    def peek(self):
        if self._count > 0:
            return self._queue[self._first_element]
        else:
            while True:
                pass
            raise Exception("Empty array")

    def empty(self):
        return self._count == 0

    def clean(self):
        self._queue = []
        self._count = 0
        self._first_element = 0

queue = Queue()

check_list = [0] * 10000011

check_list[1] = 1
check_list[2] = 2
check_list[3] = 3

repeated_numbers = [False] * 10000011

m = 2
queue.enqueue(m)
for k in range(2, 1000000):
    iteration = 2
    product = iteration * m
    while iteration <= m and product <= 1000000:
        if not repeated_numbers[product]:
            check_list[product] = check_list[m] + 1
            repeated_numbers[product] = True
            queue.enqueue(product)
        iteration += 1
        product = iteration * m
    if not repeated_numbers[m + 1]:
        repeated_numbers[m + 1] = True
        queue.enqueue(m + 1)
        check_list[m + 1] = check_list[m] + 1
    queue.dequeue()
    m = queue.peek()

for i in range(int(input())):
    n = int(input())
    print(check_list[n])