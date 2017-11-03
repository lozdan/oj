# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Insert a node at a specific position in a linked list
# problem url: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
# date: 9/3/2017

 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def insertNth(head, data, position):
    current = head
    count = 1
    if head is None:
        return Node(data)
    elif position == 0:
        head = Node(data, head)
        return head
    else:
        while count < position:
            current = current.next
            count += 1
        current_2 = current.next
        current.next = Node(data, current_2)
        return head