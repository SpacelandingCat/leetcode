class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num = []
        result = []
        
        for i in range(len(nums)):
            num.append(nums[i] ** 2)
            
        s = num.index(min(num))
        l = s - 1
        r = s + 1
        result.append(num[s])
        while l > -1 and r < len(num):
            if num[l] < num[r]:
                result.append(num[l])
                l -= 1
            else:
                result.append(num[r])
                r += 1
        if l > -1:
            for i in reversed(range(l+1)):
                result.append(num[i])
        if r < len(num):
            for i in range(r, len(num)):
                result.append(num[i])
        return result