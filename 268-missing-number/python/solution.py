from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        seq_sum = int((n * (n + 1)) / 2)

        rest = seq_sum
        for a in nums:
            rest -= a

        return rest
