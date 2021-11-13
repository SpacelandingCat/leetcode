class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = ''
        result = 0
        for i in s:
            if i not in ss:
                ss += i
            else:
                result = len(ss) if len(ss) > result else result
                ss = ss[ss.index(i)+1:len(ss)]+i
        result = len(ss) if len(ss) > result else result
        return result