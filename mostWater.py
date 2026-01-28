def maxArea(height):
    start = 0
    end = len(height) - 1
    result = -10000
    while(start < end):
        w = end - start
        h = min(height[start], height[end])
        ans = w * h
        result = max(result, ans)
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1

    return result

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
ans = maxArea(height)
print("Container with max water is: ", ans)
