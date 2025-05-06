def best_profit(prices):
    n = len(prices)
    best = 0
    for i in range(n):
        for j in range(i + 1, n):  # Try selling at all future prices
            best = max(best, prices[j] - prices[i])  # Update max profit
    return best

def best_profit(prices):
    n = len(prices)
    best = 0
    for i in range(n):
        min_price = min(prices[0:i+1])  # Find min price up to day i
        best = max(best, prices[i] - min_price)  # Max profit if selling at day i
    return best

def best_profit(prices):
    n = len(prices)
    best = 0
    min_price = prices[0]
    for i in range(n):
        min_price = min(min_price, prices[i])  # Update min price seen so far
        best = max(best, prices[i] - min_price)  # Update best profit
    return best

#| Version | Time Complexity | Description                |
#| ------- | --------------- | -------------------------- |
#| 1       | O(n²)           | Try all buy/sell pairs     |
#| 2       | O(n²)           | Recalculates min each step |
#| 3 ✅     | O(n)            | Keeps track of min so far  |
