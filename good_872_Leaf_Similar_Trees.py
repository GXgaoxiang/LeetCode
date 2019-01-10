# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        ls_root1 = []
        ls_root2 = []
        self.get_ls(root1,ls_root1)
        self.get_ls(root2,ls_root2)
        return ls_root1==ls_root2
    def get_ls(self,root,ls_root):
        if root == None:
            return
        elif root.left == None and root.right == None:
            ls_root.append(root.val)
            return
        elif root.left == None and root.left !=None:
            self.get_ls(root.left,ls_root)
        elif root.left != None and root.left ==None:
            self.get_ls(root.right,ls_root)
        else:
            self.get_ls(root.left,ls_root)
            self.get_ls(root.right,ls_root) 
