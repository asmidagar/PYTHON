#Leetcode 230
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        L = []

        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            L.append(root.val)
            inorder(root.right)

        inorder(root)
        return L[k-1]
