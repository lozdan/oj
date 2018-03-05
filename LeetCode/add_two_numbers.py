# author: Daniel Lozano
# source: LeetCode ( https://www.leetcode.com )
# problem name: Problems > Add Two Numbers
# problem url: https://leetcode.com/problems/add-two-numbers/description/

class Solution:
    def addTwoNumbers(self, l1, l2):
        number_1 = self.linked_list_to_int(l1)
        number_2 = self.linked_list_to_int(l2)
        add = list(reversed(str(number_1 + number_2)))
        
        answer = ListNode(add[0])
        current = answer
        for i in range(1, len(add)):
            current.next = ListNode(add[i])
            current = current.next
        
        return answer
    
    def linked_list_to_int(self, linked_list):
        number = ""
        while linked_list is not None:
            number += str(linked_list.val)
            linked_list = linked_list.next
        return int("".join(reversed(number)))