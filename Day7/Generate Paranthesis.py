class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, ans, s1, s2, n):
            if len(curr) == 2 * n:
                ans.append(curr)
                return
            if s1 < n:
                backtrack(curr + "(", ans, s1 + 1, s2, n)
            if s2 < s1:
                backtrack(curr + ")", ans, s1, s2 + 1, n)
        
        ans = []
        backtrack("", ans, 0, 0, n)
        return ans