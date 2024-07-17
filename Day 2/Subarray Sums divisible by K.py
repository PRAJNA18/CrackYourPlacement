class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        p = 0 
        r = 0  
        m = [0] * k 
        m[0] = 1

        for n in nums:
            p = (p + n % k + k) % k
            r += m[p]
            m[p] += 1

        return r