#Leetcode 525

class Solution:
    def findMaxLength(self, nums):
        mp = {}
        total = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                total -= 1
            else:
                total += 1

            if total == 0:
                max_len = i + 1
            elif total in mp:
                max_len = max(max_len, i - mp[total])
            else:
                mp[total] = i

        return max_len