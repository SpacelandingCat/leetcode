class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxs = [-float('inf'),-float('inf'),-float('inf')]
        m = 0
        for i in range(len(nums)):
            if nums[i] not in maxs:
                if m < 3 :
                    maxs[m] = nums[i]
                    m += 1
                    if m == 3:
                        maxs = sorted(maxs)
                else:
                    if nums[i] > maxs[0]:
                        j = len(maxs) - 1
                        while j >= 0:
                            if nums[i] > maxs[j]:
                                for k in range(j):
                                    maxs[k] = maxs[k+1]
                                maxs[j] = nums[i]
                                break
                            j -= 1
        if m > 2:
            return maxs[0]
        else:
            if maxs[0] > maxs[1]:
                return maxs[0]
            else:
                return maxs[1]