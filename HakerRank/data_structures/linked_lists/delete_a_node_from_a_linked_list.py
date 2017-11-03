# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Delete a Node
# problem url: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
# date: 9/3/2017
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def deletion_element(head, position):
    if position == 0:
        return head.next
    else:
        count = 1
        current = head
        while count < position:
            current = current.next
            count += 1
        current.next = current.next.next
        print_list(head)