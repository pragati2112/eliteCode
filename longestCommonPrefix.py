def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        
        strs.sort()
        print(strs)
        
        p = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y: p+=x
            else: break
        return p



strs = ["aac","acab","aa","abba","aa"]


print(longestCommonPrefix(strs))        