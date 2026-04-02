#Leetcode 39
class Solution:
    def combinationSum(self, candidates, target):
        result = []
        temp = []

        def helper(index, target):
            if target == 0:
                result.append(temp[:])
                return
            
            if index >= len(candidates) or target < 0:
                return
            temp.append(candidates[index])
            helper(index, target - candidates[index])
            temp.pop()
            helper(index + 1, target)

        helper(0, target)
        return result