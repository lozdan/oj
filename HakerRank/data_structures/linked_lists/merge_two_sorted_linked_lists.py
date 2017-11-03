# author: Daniel Lozano
# source: HAckerRank ( https://www.hackerrank.com )
# problem name: Data Structures: Linked Lists: Merge two sorted linked lists
# problem url: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
# date: 9/4/2017

 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
       
def MergeLists(headA, headB):
    if not headB:
        return headA
    elif not headA:
        return headB
    else:
        current = Node()
        while headA or headB:
            if headA and headB and headA.data <= headB.data:
                insert_tale(current, headA.data)
                headA = headA.next
            elif headA and headB and headB.data <= headA.data:
                insert_tale(current, headB.data)
                headB = headB.next
            elif headA:
                insert_tale(current, headA.data)
                headA = headA.next
            else:
                insert_tale(current, headB.data)
                headB = headB.next
        return current.next
  

def insert_tale(head, data):
    instance_2 = Node(data)
    current = head
    if head is None:
        return instance_2
    else:
        while current.next is not None:
            current = current.next
        current.next = instance_2
        return head