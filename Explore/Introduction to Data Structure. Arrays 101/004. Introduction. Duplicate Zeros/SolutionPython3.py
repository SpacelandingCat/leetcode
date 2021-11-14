class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                for j in reversed(range(i+1, len(arr))):
                    arr[j] = arr[j-1]
                i += 1
            i += 1
			
    def duplicateZerosAlternate(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
			arr_c = arr[i:len(arr)]
            if 0 in arr_c:
                i += arr_c.index(0)
                for j in reversed(range(i+1, len(arr))):
                    arr[j] = arr[j-1]
                i += 2
            else:
                i = len(arr)