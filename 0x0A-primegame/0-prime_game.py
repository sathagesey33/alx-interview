#!/usr/bin/python3
"""Prime Game."""


def isWinner(x, nums):
    """function that checks for the winner"""
    if not nums or x < 1:
        return None
    max_num = max(nums)

    filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            filter[j] = False
    filter[0] = filter[1] = False
    y = 0
    for i in range(len(filter)):
        if filter[i]:
            y += 1
        filter[i] = y
    player1 = 0
    for x in nums:
        player1 += filter[x] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
