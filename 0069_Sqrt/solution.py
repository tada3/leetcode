from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        p = 2
        while p < x:
            #print(f'x = {x}, p = {p}')
            pp = p * p
            if pp < x:
                if 4 * pp < x:
                    p = 2 * p
                else:
                    p += 1
                continue
            if pp == x:
                return p
            else:
                return p - 1
            
        return 1

def main(x):
    print(f'Input: x = {x}')
    ret = Solution().mySqrt(x)
    print(f'Output: {ret}')

if __name__ == "__main__":
    #x = 4
    #x = 8
    x = 0
    #x = 16
    #x = 144
    #x = 6
    main(x)