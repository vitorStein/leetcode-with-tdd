class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        for index, _ in enumerate(nums):
            if sum(nums[:index]) == sum(nums[index + 1:]):
                return index
            
        return -1

