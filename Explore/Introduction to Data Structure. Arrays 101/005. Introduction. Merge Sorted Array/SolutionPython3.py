class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cm = 0
        cn = 0
        while cm < m and cn < n:
            if nums1[cm] > nums2[cn]:
                for i in reversed(range(cm+1, len(nums1))):
                    nums1[i] = nums1[i-1]
                nums1[cm] = nums2[cn]
                m += 1
                cm += 1
                cn += 1
            else:
                cm += 1
        while cn < n:
            nums1[cm] = nums2[cn]
            cm += 1
            cn += 1
