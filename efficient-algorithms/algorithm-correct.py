import random

# Brute force version – O(n²)
def best_profit_brute(prices):
    n = len(prices)
    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            best = max(best, prices[j] - prices[i])
    return best

# Fast version – O(n)
def best_profit_fast(prices):
    if not prices:
        return 0
    min_price = prices[0]
    best = 0
    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best

# Auto-testing both functions with random inputs
while True:
    n = random.randint(1, 20)
    prices = [random.randint(1, 10) for _ in range(n)]

    result_brute = best_profit_brute(prices)
    result_fast = best_profit_fast(prices)

    print(prices, result_brute, result_fast)

    if result_brute != result_fast:
        print("❌ ERROR: Results do not match!")
        break
