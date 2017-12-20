# author: Daniel Lozano
# source: HackerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Compare two linked lists
# problem url: https://www.hackerrank.com/challenges/compare-two-linked-lists/problem
# date: 9/4/2017

 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def CompareLists(headA, headB):
    if not headA and not headB:
        return 1
    elif headA and headB:
        if headA.data != headB.data:
            return 0
        return CompareLists(headA.next, headB.next)
    else:
        return 0