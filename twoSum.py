#Approach 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    L.append(i)
                    L.append(j)

        
        return L

#Approach 2(Optimized)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        index = 0
        while index < len(nums):
            res = target - nums[index]
            if res in num_map:
                return [num_map[res], index]
            num_map[nums[index]] = index
            index += 1
        return []
        