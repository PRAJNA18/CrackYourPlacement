class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        r1 = m - 1
        r2 = n - 1
        w = m + n - 1

        while r1 >= 0 and r2 >= 0 and w >= 0:
            if nums2[r2] > nums1[r1]:
                nums1[w] = nums2[r2]
                r2 -= 1
            elif nums1[r1] >= nums2[r2]:
                nums1[w] = nums1[r1]
                r1 -= 1
            w -= 1

        while r2 >= 0:
            nums1[w] = nums2[r2]
            r2 -= 1
            w -= 1