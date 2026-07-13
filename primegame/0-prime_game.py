#!/usr/bin/python3
"""Prime Game module."""


def isWinner(x, nums):
    """Return the player who wins the most rounds of the prime game."""
    if not nums or x <= 0:
        return None

    rounds = x
    if rounds > len(nums):
        rounds = len(nums)

    max_n = 0
    for index in range(rounds):
        if nums[index] > max_n:
            max_n = nums[index]

    if max_n < 2:
        return "Ben" if rounds else None

    primes = [True] * (max_n + 1)
    primes[0] = False
    primes[1] = False

    number = 2
    while number * number <= max_n:
        if primes[number]:
            multiple = number * number
            while multiple <= max_n:
                primes[multiple] = False
                multiple += number
        number += 1

    prime_counts = [0] * (max_n + 1)
    count = 0
    for number in range(max_n + 1):
        if primes[number]:
            count += 1
        prime_counts[number] = count

    maria_wins = 0
    ben_wins = 0

    for index in range(rounds):
        if prime_counts[nums[index]] % 2:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None