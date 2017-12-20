# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Print the Elements of a Linked List
# problem url: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
# date: 9/1/2017
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
       
def print_list(head):
    while head != None:
        print(head.data)
        head = head.next