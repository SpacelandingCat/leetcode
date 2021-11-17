class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        rs = set(nums)
        res = []
        for i in range(1,len(nums)+1):
            if i not in rs:
                res.append(i)
        return res
	
    def findDisappearedNumbersWithoutExtraSpace(self, nums: List[int]) -> List[int]:
        rs = set(nums)
        for i in range(1,len(nums)+1):
            if i not in rs:
                rs.add(i)
            else:
                rs.remove(i)
        return rs