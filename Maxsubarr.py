def maxSub(nums):
    mv = nums[0]
    sum = 0
    for v in nums:
        sum += v
        mv = max(mv, sum)
        if sum < 0:
            sum = 0

    return mv

L = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ans =maxSub(L)
print(ans)