#Leetcode 560
#Solution but with TLE 
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       n = len(nums)
       ans = 0
       for i in range(n):
        sum = nums[i]
        if sum == k:
            ans += 1

        for j in range(i+1, n):
            sum += nums[j]
            if sum == k:
                ans += 1

       return ans 

#Without TLE
class Solution:
    def subarraySum(self, nums, k):
        sum1 = 0
        count = 0
        Hmap = {0: 1} 

        for num in nums:
            sum1 += num
            if (sum1 - k) in Hmap:
                count += Hmap[sum1 - k]
            Hmap[sum1] = Hmap.get(sum1, 0) + 1

        return count