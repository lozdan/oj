# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Queues: Queue using Two Stacks
# problem url: https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
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
            raise Exception("Empty queue")

    def peek(self):
        if self._count > 0:
            return self._queue[self._first_element]
        else:
            raise Exception("Empty queue")



queue = Queue()


for i in range(int(input())):
    operation = input().split()
    if operation[0] == "1":
        queue.enqueue(int(operation[1]))
    elif operation[0] == "2":
        queue.dequeue()
    elif operation[0] == "3":
        print(queue.peek())