def maxProduct(nums):
    minV = maxV = ans = nums[0]

    for i in range(1, len(nums)):
        d = nums[i]
        tempM = max(minV*d, maxV*d, d)
        tempm = min(minV*d, maxV*d, d)
        maxV = tempM
        minV = tempm
        ans = max(ans, maxV)

    return ans

nums = [2, 3, -2, 4]
a = maxProduct(nums)
print(a)