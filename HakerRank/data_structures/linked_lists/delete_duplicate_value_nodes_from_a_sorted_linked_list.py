# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Delete duplicate-value nodes from a sorted linked list
# problem url: https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem
# date: 9/5/2017

 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
       
def RemoveDuplicates(head):
    current = head
    while current.next:
        if current.next.data == current.data:
            current.next = current.next.next
        else:
            current = current.next
    return head