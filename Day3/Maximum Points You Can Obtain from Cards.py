class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ls, rs, n = sum(cardPoints[:k]), 0, len(cardPoints)
        res = ls
        for i in range(k):
            ls -= cardPoints[k - i -1]
            rs += cardPoints[n - i - 1]
            res = max(res, ls + rs)
        return res