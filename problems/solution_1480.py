class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        for index, value in enumerate(nums):
            if index == 0:
                result.append(value)
            else:
                result.append(value + result[index - 1])

        return result