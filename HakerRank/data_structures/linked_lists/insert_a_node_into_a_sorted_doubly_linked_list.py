# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Inserting a Node Into a Sorted Doubly Linked List
# problem url: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem
# date: 9/7/2017

 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node
       
def SortedInsert(head, data):
    if head is None:
        head = Node(data)
        return head
    else:
        current = head
        while current is not None:
            if current.next is None or data <= current.next.data:
                current.next = Node(data, current.next)
                current.next.prev = current
                return head
            current = current.next