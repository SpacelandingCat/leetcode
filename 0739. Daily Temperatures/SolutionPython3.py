class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []        
        pr = {}
        tl = len(temperatures)
        ttt = set(temperatures)
        for p in ttt:
            pr[p] = temperatures.index(p)
            temperatures.append(p)
        ppr = list(pr.keys())
        ppr.sort()
        
        i = 0
        while i < tl:
            c = tl
            ct = temperatures[i]
            pr[ct] = temperatures.index(ct,pr[ct]+1)
            if pr[ct] >= tl:
                pr[ct] = -1
            j = ppr.index(ct)+1
            while j < len(ppr):
                if ppr[j] > ct:
                    if pr[ppr[j]] > 0:
                        if pr[ppr[j]] - i  < c:
                            c = pr[ppr[j]] - i
                j += 1
            if c == tl:
                c = 0
            result.append(c)
            i += 1
        return result