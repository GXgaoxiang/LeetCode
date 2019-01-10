# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        faster_node, lower_node = head,head
        while faster_node != None and faster_node.next!=None:
            lower_node = lower_node.next
            faster_node = faster_node.next.next
        return lower_node

# 要学会利用快慢指针。 用两个指针来取得中间值
