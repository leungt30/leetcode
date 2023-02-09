class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        special = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        regular = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range (len(s)):
            c=s[i]
            s2 = s[i:i+2]
            if s2 in special.keys():
                counter += special[s2] - regular[s[i+1]]
            elif s[i] in regular:
                counter += regular[s[i]]
        return counter

        
        