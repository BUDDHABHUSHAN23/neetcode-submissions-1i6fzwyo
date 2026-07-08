class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # v.1.1
        lenA = len(nums1)
        lenB = len(nums2)
        merged = nums1 + nums2
        merged.sort()

        total = len(merged)

        # if odd retert the midean as middle element 
        if total % 2 == 0 :
            return (merged[total // 2  - 1] + merged[total // 2]) /  2.0
        else :
            return merged[total //2]
            