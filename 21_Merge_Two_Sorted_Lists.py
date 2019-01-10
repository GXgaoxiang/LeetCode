# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 == None:
        return l2
    elif l2 == None:
        return l1
    elif l1 == None and l2 == None:
        return []

    if l1.val <= l2.val:
        ln = ListNode(l1.val)
        p = ln
        l1 = l1.next
    else:
        ln = ListNode(l2.val)
        p = ln
        l2 = l2.next
    while l1 != None and l2 != None:
        if l1.val <= l2.val:
            ln.next = ListNode(l1.val)
            ln = ln.next
            l1 = l1.next
        else:
            ln.next = ListNode(l2.val)
            ln = ln.next
            l2 = l2.next
    if l1 != None:
        ln.next = l1
    if l2 != None:
        ln.next = l2
    return p
