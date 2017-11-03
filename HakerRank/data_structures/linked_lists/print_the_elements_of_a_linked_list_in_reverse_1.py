# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Print in Reverse
# problem url: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem
# date: 9/3/2017

 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
       
def ReversePrint(head):
    if head is None:
        return False
    else:
        current = None
        while head is not None:
            prox = head.next
            head.next = current
            current = head
            head = prox
        while current:
            print(current.data)
            current = current.next