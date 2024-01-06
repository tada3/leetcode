from typing import List
from collections import deque

class Solution:
    # Optimized for this problem
    # Case 1: all '9', answer is '1000..'
    # Case 2: Find the lowest non-'9'. 
    #   Suppose that digit is '6', answer is '????70000..'.
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0 and digits[i] == 9:
            i -= 1
        
        # Case 1
        if i < 0:
            result = [0] * (len(digits) + 1)
            result[0] = 1
            return result
        
        # Case 2
        result = [0] * len(digits)
        for j in range(0, i):
            result[j] = digits[j]
        result[i] = digits[i] + 1
        return result        


    # Straight forward way
    def plusOneSF(self, digits: List[int]) -> List[int]:
        result = []
        add = True
        for i in range(len(digits)-1, -1, -1):
            x = digits[i]
            if add:
                x += 1
            if x >= 10:
                add = True
                x -= 10
            else:
                add = False
            result.append(x)            
        if add:
            result.append(1)
        result.reverse()
        return result



def main(digits):
    print(f'Input: digitis = {digits}')
    ret = Solution().plusOne(digits)
    print(f'Output: {ret}')




if __name__ == "__main__":
    digits = [1,2,3]
    #digits = [4,3,2,1]
    #digits = [9]
   
    main(digits)