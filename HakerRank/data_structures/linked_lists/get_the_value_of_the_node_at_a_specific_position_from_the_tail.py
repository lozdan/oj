# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Get Node Value
# problem url: https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem
# date: 9/5/2017

 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
       
def GetNode(head, position):
    current = None
    while head:
        prox = head.next
        head.next = current
        current = head
        head = prox
    
    count = 0
    while count < position:
        current = current.next
        count += 1
    return current.data