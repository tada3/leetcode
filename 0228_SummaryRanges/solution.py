from typing import List

class Solution:
    # In LeetCode, this is faster (40ms) than summaryRengesXXX(around 60ms).
    # But substantially the same.
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ret = []
        N = len(nums) 
        if N == 0:
            return ret

        start = 0
        while True:
            i = start + 1
            while i<N and nums[i] - nums[i-1] == 1:
                i += 1
            ret.append(str(nums[start]) if i-1==start else f'{nums[start]}->{nums[i-1]}')
            if i == N:
                break
            start = i

        return ret
    
        
    def summaryRangesXXX(self, nums: List[int]) -> List[str]:
        ret = []
        if len(nums) == 0:
            return ret
        
        a = nums[0]
        b = a
        for x in nums[1:]:
            if x == b + 1:
                # extend the range
                b = x
            else:
                # close the current range and create a new range
                ret.append(str(a) if a==b else f'{a}->{b}')
                a = x
                b = x

        ret.append(str(a) if a==b else f'{a}->{b}')
        return ret


def main(nums):
    print(f'Input: nums = {nums}')
    ret = Solution().summaryRanges(nums)
    print(f'Output: {ret}')




if __name__ == "__main__":
    nums = [0,1,2,4,5,7]
    #nums = [0,2,3,4,6,8,9]
    #nums = []
    #nums = [-100]
    #nums = [-10,-9,-8]
    main(nums)