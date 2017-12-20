# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Reverse a doubly linked list
# problem url: https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
# date: 9/7/2017

 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

def Reverse(head):
    if head is None:
        return head
    else:
        current = None
        while head:
            pref = head.next
            head.next = head.prev
            current = head
            head = pref
            current.prev = head
        return current