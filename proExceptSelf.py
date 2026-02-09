def productExceptSelf(nums):
    n = len(nums)
    ans = [1]*n

    for i in range(1, n):
        ans[i] = nums[i-1] * ans[i-1]

    s = 1
    for j in range(n - 2, -1, -1):
        s = s * nums[j+1]
        ans[j] = ans[j] * s

    return ans

nums = [1, 2, 3, 4]
ans1 = productExceptSelf(nums)
print(ans1)