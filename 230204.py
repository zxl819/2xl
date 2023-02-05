from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        x = 0
        for y in coins:
            if y <= (x+1):
                x = y+x
            else:
                break
        return x+1

coins = [1,1,1,4]
print(Solution().getMaximumConsecutive(coins=coins))

