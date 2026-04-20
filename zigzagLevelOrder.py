# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            count = 0
            ans = []
            tempAns = []
            if root is None:
                return []
            q = deque([root, None])
            while q:
                temp = q.popleft()
                if temp is None:
                    if tempAns:
                        if count % 2 == 1:
                            tempAns = tempAns[::-1]
                        ans.append(tempAns[:])
                        tempAns.clear()
                        count += 1
                        if q:
                            q.append(None)

                else:
                    tempAns.append(temp.val)
                    if temp.left:
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)

            return ans
            
