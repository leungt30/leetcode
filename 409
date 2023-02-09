class Solution:
    def longestPalindrome(self, s: str) -> int:
        mapping = {}
        for letter in s:
            if (letter not in mapping.keys()):
                mapping[letter]=1
            else:
                mapping[letter]+=1
        oddFound = False
        sum = 0

        for value in mapping.values():
            if (value % 2 == 0):
                sum += value
            elif (not oddFound):
                sum += value
                oddFound= True
            else:
                sum += value-1
        return sum