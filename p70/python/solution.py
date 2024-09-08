from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        stairs = [0] * n

        stairs[0] = 1
        stairs[1] = 1

        for i in range(0, n - 1):
            stairs[i + 1] += stairs[i]
            if i + 2 < n:
                stairs[i + 2] += stairs[i]

        return stairs[n - 1]
