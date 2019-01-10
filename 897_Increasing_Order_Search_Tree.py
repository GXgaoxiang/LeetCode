# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ls_number = []
        self.search(root, ls_number)
        for i in range(len(ls_number)):
            if i == 0:
                node = TreeNode(ls_number[i])
                temp = node
            else:
                n = TreeNode(ls_number[i])
                temp.right = n
                temp = n
        return node

    def search(self, root, ls_number):
        if root == None:
            return
        else:

            self.search(root.left, ls_number)
            ls_number.append(root.val)
            self.search(root.right, ls_number)