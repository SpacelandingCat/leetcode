class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        l = len(nums)
        for i in range(1,l):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        return k+1