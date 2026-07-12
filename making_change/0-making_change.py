#!/usr/bin/python3
"""
Making Change Module
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.
    """
    if total <= 0:
        return 0
    coins = sorted(list(set(coins)))
    if not coins:
        return -1
    largest_coin = coins[-1]
    buffer = largest_coin * 2
    if len(coins) > 1:
        buffer = largest_coin * coins[-2]
    if total > buffer:
        k = (total - buffer) // largest_coin
        total = total - k * largest_coin
    else:
        k = 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            val = dp[amount - coin] + 1
            if val < dp[amount]:
                dp[amount] = val
    if dp[total] == float('inf'):
        return -1
    return dp[total] + k
