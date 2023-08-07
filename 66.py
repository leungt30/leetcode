#recursive solution to problem
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #case 1: only a single digit remains and it will not cause any carry
        if digits[-1] !=9:
            digits[-1] += 1
            return digits
        else:
            #case 2: a carry will be involved (the last digit is a 9)
            if len(digits) != 1:
                #case 2.1: last digit is 9 but there are digits greater than it, carry must be passed on.
                digits = self.plusOne(digits[0:-1])
                digits.append(0)
                return digits
            #case 2.2: the last digit remaining is a 9, hence when adding we get 10
            return [1,0]