from typing import List


class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            expected = i + 1

            while True:
                current = nums[i]

                if current != expected and current != nums[current - 1]:
                    nums[i], nums[current - 1] = nums[current - 1], nums[i]
                else:
                    break

        result = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(i + 1)

        return result
