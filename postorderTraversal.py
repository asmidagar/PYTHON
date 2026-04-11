#leetcode 145
#approach 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root, result):
            if root == None:
                return
            postorder(root.left, result)
            postorder(root.right, result)
            result.append(root.val)

        result = []
        postorder(root, result)
        return result 
    
#approach 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def postorder(root):
            if root != None:
                postorder(root.left)
                postorder(root.right)
                result.append(root.val)

        postorder(root)
        return result 
    