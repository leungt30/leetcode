class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        upLim = int(-1 * (1-(1+8*n)**(0.5))/2)

        count = 1
        for i in range(2,upLim+1):
            if self.possible(n,i):
                count+=1
        return count

    
    def possible(self, n, div):
        return (div%2==0 and n%div == div/2) or (div%2==1 and n%div==0)

