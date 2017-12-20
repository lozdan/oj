# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Find Merge Point of Two Lists
# problem url: https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
# date: 9/6/2017

 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def FindMergeNode(headA, headB):
    current = headA
    while current.next != headB.next:
        while current:
            if current.next == headB.next:
                return current.next.data
            current = current.next
        current = headA
        headB = headB.next