class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return (self.helper(s,t) and self.helper(t,s))
    def helper(self,s,t):
        mapping = {}
        for i in range(len(s)):
            if not s[i] in mapping.keys():
                mapping[s[i]] = t[i]
            else:
                if mapping[s[i]] != t[i]:
                    return False
        return True