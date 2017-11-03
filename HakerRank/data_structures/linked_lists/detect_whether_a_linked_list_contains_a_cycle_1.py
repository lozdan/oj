# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Cycle Detection
# problem url: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
# date: 9/6/2017

 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
       
def has_cycle(head):
    cheking_list = set()
    while head:
        if head in cheking_list:
            return True
        else:
            cheking_list.add(head)
            head = head.next
    return False