# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Insert a Node at the Tail of a Linked List
# problem url: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
# date: 9/1/2017

 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
       
def Insert(head, data):
    instance = Node(data)
    current = head
    if head is None:
        return instance
    else:
        while current.next is not None:
            current = current.next
        current.next = instance
        return head