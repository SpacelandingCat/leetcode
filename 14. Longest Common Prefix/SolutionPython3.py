class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        i = 1
        while i <= len(strs[0]):
            result = strs[0][0:i]
            for s in strs:
                if s[0:i] != result:
                    result = strs[0][0:i-1]
                    return result
            i += 1
        return result