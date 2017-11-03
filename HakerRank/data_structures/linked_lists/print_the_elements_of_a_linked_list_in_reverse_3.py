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
        current = head
        while head.next is not None:
            while current.next.next is not None:
                current = current.next
            print(current.next.data)
            current.next = None
            current = head
        print(head.data)