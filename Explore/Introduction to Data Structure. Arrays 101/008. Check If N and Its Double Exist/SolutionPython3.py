class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0
        j = 0
        r = False
        while i < len(arr)-1 and r == False:
            j = i + 1
            while j < len(arr):
                if arr[j] == arr[i] * 2 or arr[i] == arr[j] * 2:
                    r = True
                    break
                j += 1
            i += 1
        return r