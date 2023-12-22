from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        for y in range(x, 2, -1):
            sqrt = 1
            tmp = 0
            p = 2
            z = y
            while p <= z:
                d, m = divmod(z, p)
                print(f'y = {y}, z = {z}, p = {p}, d={d}, m={m}')
                if m == 0:
                    z = d
                    if tmp != 0:
                        if tmp == p:
                            sqrt *= p
                            if sqrt * sqrt == y:
                                return sqrt
                            tmp = 0
                        else:
                            break
                    else:
                        tmp = p
                else:
                    if tmp != 0:
                        break
                    p += 1    
     
        return 1

def main(x):
    print(f'Input: x = {x}')
    ret = Solution().mySqrt(x)
    print(f'Output: {ret}')

if __name__ == "__main__":
    #x = 4
    #x = 8
    #x = 1
    #x = 16
    #x = 144
    x = 6
    main(x)