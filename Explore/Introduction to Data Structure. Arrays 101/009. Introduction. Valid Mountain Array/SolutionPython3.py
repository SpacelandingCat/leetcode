class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        m = -1
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                m = i
            else:
                break
        if m == -1 or m == len(arr) - 1:
            return False
        for i in range(m+1, len(arr)):
            if arr[i] < arr[i-1]:
                m = i
            else:
                break
        if m < len(arr) - 1:
            return False
        else:
            return True
