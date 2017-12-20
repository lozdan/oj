# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Cycle Detection
# problem url: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
# date: 9/6/2017

 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
       
def has_cycle(head):
    cheking_list = [0] * 100
    count = 0
    while head:
        if head in cheking_list:
            return True
        else:
            cheking_list[count] = head
            head = head.next
            count += 1
    return False