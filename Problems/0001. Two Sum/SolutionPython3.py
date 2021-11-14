class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            if target - i in nums:
                j = len(nums) - 1 - nums[::-1].index(i)
                if nums.index(target - i) != j:
                    return [j,nums.index(target - i)]
