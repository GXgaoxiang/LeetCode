"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# 运用递归的思想进行解答
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        elif root.children == []:
            return 1
        depth = 1 + max(self.maxDepth(child) for child in root.children)
        return depth
