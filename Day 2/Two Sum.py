class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, j in enumerate(nums):
            if check and target - j in check:
                return [i, check[target - j]]
            check[j] = i