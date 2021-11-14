class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        pal_s = set(s)
        if len(pal_s) == 1:
            return s
        for ind_c in range(len(s)):
            pal = ''
            ind_l = ind_c
            ind_r = ind_c + 1
            while ind_l > -1 and ind_r < len(s):
                if s[ind_l] == s[ind_r]:
                    pal = s[ind_l] + pal + s[ind_r]
                    ind_l -= 1
                    ind_r += 1
                else:
                    break
            if len(result) < len(pal):
                result = pal
            pal = s[ind_c]
            ind_l = ind_c - 1
            ind_r = ind_c + 1
            while ind_l > -1 and ind_r < len(s):
                if s[ind_l] == s[ind_r]:
                    pal = s[ind_l] + pal + s[ind_r]
                    ind_l -= 1
                    ind_r += 1
                else:
                    break
            if len(result) < len(pal):
                result = pal
        return result