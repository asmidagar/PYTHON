def maxProfit(List):
    buy = List[0]
    pr = 0
    for i in range(1, len(List)):
        sell = List[i]
        if sell > buy:
            pr = max(pr, (sell - buy))
        if buy > List[i]:
            buy = List[i]

    return pr

List = [7, 1, 5, 3, 6, 4]
ans = maxProfit(List)
print("Max profit is: ", ans)
