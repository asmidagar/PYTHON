def majority(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    even = 0
    n = len(nums)
    if n % 2 == 0:
        even = 1

    for key in d:
        c = d[key]
        if c >= n // 2 and even == 1 or c > n//2:
            return key

List = [6, 5, 5]
ans = majority(List)
print(ans)
    