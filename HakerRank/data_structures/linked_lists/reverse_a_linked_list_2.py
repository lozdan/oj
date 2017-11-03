# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Reverse a linked list
# problem url: https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
# date: 9/4/2017
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def Reverse(head):
    if head is None:
        return head
    else:
        current = None
        while head is not None:
            current = Node(head.data, current)
            head = head.next
        return current
  