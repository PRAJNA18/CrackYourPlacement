class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        t = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[t], nums[i] = nums[i], nums[t]
                t += 1