# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        count_1 = 0
        index_1 = 0
        while (l1 != None):
            count_1 += l1.val * (10 ** index_1)
            l1 = l1.next
            index_1 += 1
        count_2 = 0
        index_2 = 0
        while (l2 != None):
            count_2 += l2.val * (10 ** index_2)
            l2 = l2.next
            index_2 += 1
        amount = count_1 + count_2

        a = amount % 10
        amount = amount // 10
        l3 = ListNode(a)
        temp = l3
        while amount > 0:
            n = amount % 10
            temp.next = ListNode(n)
            temp = temp.next
            amount = amount // 10
        return l3




