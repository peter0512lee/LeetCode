class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        total_len = len(merged)
        
        if total_len % 2 == 0:
            return (merged[total_len // 2 - 1] + merged[total_len // 2]) / 2.0
        else:
            return merged[total_len // 2]