#Leetcode 128

class Solution:
    def longestConsecutive(self, nums):
        st = set(nums)
        longest = 0

        for num in st:
            if (num - 1) not in st:
                current_num = num
                current_streak = 1

                while (current_num + 1) in st:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest