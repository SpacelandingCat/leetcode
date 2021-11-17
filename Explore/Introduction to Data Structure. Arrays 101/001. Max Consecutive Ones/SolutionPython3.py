class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        counter = 0
        for i in nums:
            if i == 1:
                counter += 1
            else:
                if counter > result:
                    result = counter
                counter = 0
        if counter > result:
            return counter
        else:
            return result