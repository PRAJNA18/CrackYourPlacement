class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, total = 0, 0
        d = {0 : 1}
        
        for i in nums:
            total += i
            if total - k in d:
                res += d[total - k]
            d[total] = 1 + d.get(total, 0)

        return res