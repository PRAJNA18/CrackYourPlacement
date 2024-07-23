class Solution:
    def reverseWords(self, s: str) -> str:
        n, i = len(s), 0
        pos = []

        while i < n:
            while i < n and s[i] == " ":
                i += 1
            if i == n:
                break

            start = i

            while i < n and s[i] != " ":
                i += 1
            end = i - 1

            pos.append((start, end))
        
        res = ""

        for i, j in reversed(pos):
            res += (s[i : j + 1] + " ")
        
        return res[:len(res) - 1]