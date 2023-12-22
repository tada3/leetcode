from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x <= 3:
            return 1
        l = 2
        h = x - 1
        while (h - l) > 1:
            m = (l + h) / 2
            if m * m <= x:
                l = m
            else:
                h = m 
        return l

def main(x):
    print(f'Input: x = {x}')
    ret = Solution().mySqrt(x)
    print(f'Output: {ret}')

if __name__ == "__main__":
    x = 4
    #x = 8
    #x = 0
    #x = 16
    #x = 144
    #x = 0
    #x = 1
    #x = 3

    main(x)