from typing import List

class Solution:
    # From bottom to top
    # Complexity is the same, but this is much simpler.
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cl = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            ll = cl
            cl = triangle[i]
            for j in range(i+1):
                cl[j] += min(ll[j], ll[j+1])
        
        return cl[0]



    # From top to bottom
    def minimumTotalTB(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        cl = triangle[0]
        for i in range(1, len(triangle)-1):
            ul = cl
            cl = triangle[i]
            cl[0] += ul[0]
            for j in range(1, len(cl) - 1):
                cl[j] += min(ul[j-1], ul[j])
            cl[-1] += ul[-1]

        ul = cl
        cl = triangle[-1]
        min_sum = cl[0] + ul[0]
        for j in range(1, len(cl) - 1):
            tmp = cl[j] + min(ul[j-1], ul[j])
            if tmp < min_sum:
                min_sum = tmp
        tmp = cl[-1] + ul[-1]
        if tmp < min_sum:
            min_sum = tmp
                    
        return min_sum
    

def main(triangle):
    print(f'Input: triangle = {triangle}')
    ret = Solution().minimumTotal(triangle)
    print(f'Output: {ret}')




if __name__ == "__main__":
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    #triangle = [[-10]]
    #triangle = [[-10], [-1, -2]]
    main(triangle)

