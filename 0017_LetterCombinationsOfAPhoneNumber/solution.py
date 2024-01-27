from typing import List
from collections import deque

class Solution:
     def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'], 
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'], 
             '5': ['j', 'k', 'l'], 
             '6': ['m', 'n', 'o'], 
             '7': ['p', 'q', 'r', 's'], 
             '8': ['t', 'u', 'v'], 
             '9': ['w', 'x', 'y', 'z']}
        
        if len(digits) == 0:
            return ""

        ret = []
        stack = deque()        
        stack.append(('', digits[0], 1))
        while stack:
            s, d, i = stack.pop()
            if i < len(digits):
                for c in phone[d]:
                    stack.append((s + c, digits[i], i+1))
            else:
                for c in phone[d]:
                    ret.append(s + c)
        return ret


def main(digits):
    print(f'Input: digits = {digits}')
    ret = Solution().letterCombinations(digits)
    print(f'Output: {ret}')




if __name__ == "__main__":
    #digits = "23"
    #digits = ""
    digits = "2"
    
    main(digits)