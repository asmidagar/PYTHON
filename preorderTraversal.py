#Leetcode 144
#approach 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root, result):
            if root == None:
                return
            result.append(root.val)
            preorder(root.left, result)
            preorder(root.right, result)

        result = []
        preorder(root, result)
        return result 
    
#approach 2
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preorder(root):
            if root != None:
                result.append(root.val)
                preorder(root.left)
                preorder(root.right)

        preorder(root)
        return result 