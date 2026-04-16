#Leetcode 113
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def helper(root, path, tar):
            if root is None:
                return
            path.append(root.val)

            if root.left is None and root.right is None:
                if sum(path) == tar:
                    res.append(path[:])

            helper(root.left, path, tar)
            helper(root.right, path, tar)
            path.pop() 
 
        helper(root, [], targetSum)
        return res

#Leetcode 437
#Leetcode 129
#Leetcode 173