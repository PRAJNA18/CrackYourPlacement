class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt, ele = 0, 0
        for i in nums:
            if cnt == 0:
                ele = i
            if i != ele:
                cnt -= 1
            else:
                cnt += 1
        return ele