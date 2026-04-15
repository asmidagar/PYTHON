#Leetcode 543
#Approach 1
class Solution:
    def height(self, root):
        if root is None:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(
            self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right),
            self.height(root.left) + self.height(root.right)
        )
    
#Approach 2(Optimized)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def height(self, root):
        if root is None:
            return 0

        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        self.ans = max(self.ans, leftHeight + rightHeight)

        return max(leftHeight, rightHeight) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.ans
