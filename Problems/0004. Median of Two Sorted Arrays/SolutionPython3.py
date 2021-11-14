class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1)+len(nums2)) % 2 == 0:
            return (sorted(nums1+nums2)[math.ceil((len(nums1)+len(nums2))/2)-1]+sorted(nums1+nums2)[math.ceil((len(nums1)+len(nums2))/2)])/2
        else:
            return sorted(nums1+nums2)[math.ceil((len(nums1)+len(nums2))/2)-1]