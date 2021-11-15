class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cp = 0
        l = len(nums)
        while cp < l:
            if nums[cp] == val:
                for i in range(cp,l-1):
                    nums[i] = nums[i+1]
                l -= 1
            else:
                cp += 1
        return cp
