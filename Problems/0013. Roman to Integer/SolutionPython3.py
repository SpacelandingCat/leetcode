class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'M' : 1000,
            'D' : 500,
            'C' : 100,
            'L' : 50,
            'X' : 10,
            'V' : 5,
            'I' : 1
        }
        r = 0
        last = float('inf')
        for sym in s:
            val = symbols[sym]
            if val > last:
                r -= 2*last
            last = val
            r += last
        return r