from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        given = [0] * N
        for i in range(1, N):
            if ratings[i] > ratings[i-1]:
                given[i] = given[i-1] + 1
        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                tmp = given[i+1] + 1
                if given[i] < tmp:
                    given[i] = tmp
        return sum(given) + N
    

def main(ratings):
    print(f'Input: ratings = {ratings}')
    ret = Solution().candy(ratings)
    print(f'Output: {ret}')




if __name__ == "__main__":
    ratings = [1,0,2]
    #ratings = [1,2,2]
    #ratings = [1,2,87,87,87,2,1]
    #ratings = [1, 2, 3, 2, 1]
   
    main(ratings)

