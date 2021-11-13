class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            i = 0
            x = str(x)
            while i < len(x)/2:
                if x[i] != x[len(x) - 1 - i]:
                    return False
                i = i+1
            return True
        return False