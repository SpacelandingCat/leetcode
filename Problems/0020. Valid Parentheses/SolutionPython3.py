class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 0:
            lastsyms = ''
            for sym in s:
                if sym in ['(','[','{']:
                    lastsyms += sym
                else:
                    if sym in [')',']','}'] and len(lastsyms) == 0 :
                        return False
                    else:
                        if lastsyms[len(lastsyms)-1] in [')',']','}']:
                            return False
                        else:
                            if (lastsyms[len(lastsyms)-1] == '(' and sym == ')') or (lastsyms[len(lastsyms)-1] == '[' and sym == ']') or (lastsyms[len(lastsyms)-1] == '{' and sym == '}'):
                                lastsyms = lastsyms[0:len(lastsyms)-1]
                            else:
                                return False
            if len(lastsyms) == 0:
                return True
            else:
                return False
        else:
            return False