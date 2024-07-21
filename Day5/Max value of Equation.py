import sys
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        a, b = 0, 1
        res = -sys.maxsize
        while a < b and b < len(points):
            diff = points[b][0] - points[a][0]
            if diff <= k:
                res = max(res, (diff + points[b][1] + points[a][1]))
                if b == len(points) - 1 or points[b][1] >= points[a][1] + diff:
                    a += 1
                else:
                    b += 1
            else:
                a += 1

            if b == a:
                b += 1
        return res