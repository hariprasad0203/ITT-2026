class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 1. Replace the zeros from index 'm' onwards with nums2
        nums1[m : m + n] = nums2

        # 2. Sort the entire array in-place
        nums1.sort()
