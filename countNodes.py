#Leetcode 222
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
            self.var = 0

    def countNodes(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if root is None:
                return 
            inorder(root.left)
            self.var += 1
            inorder(root.right)

        inorder(root)
        return self.var
        
        