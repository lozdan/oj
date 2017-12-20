# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Insert a node at the head of a linked list
# problem url: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
# date: 9/1/2017

 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def Insert(head, data):
    return Node(data, head)