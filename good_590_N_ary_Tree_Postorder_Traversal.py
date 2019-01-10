"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return []
        for child in root.children:
            # 这里用extend的原因是每次调用的时候res都被初始化成了[]，要extend之前的值才行
            res.extend(self.postorder(child))
        res.append(root.val)
        return res

