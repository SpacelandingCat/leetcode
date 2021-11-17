class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] % 2 == 0:
                i += 1
            else:
                if nums[j] % 2 == 1:
                    j -= 1
                else:
                    p = nums[j]
                    nums[j] = nums[i]
                    nums[i] = p
                    i += 1
                    j -= 1
        return nums
