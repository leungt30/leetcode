class Solution(object):

        
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        def helper(bigNum, currentNum, letter, s):
            numN = bigNum // currentNum
            s = s + letter * numN
            bigNum = bigNum % currentNum
            return [bigNum, s]

        special = {1000: "M", 900 : "CM", 500: "D", 400: "CD",100:"C",90:"XC",50:"L",
                  40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        
        ret = ""
        x = special.keys()
        x.sort(reverse=True)

        for stuff in (x):
            arr = helper(num,stuff, special[stuff], ret)
            ret = arr[1]
            num = arr[0]
        return ret
    
        