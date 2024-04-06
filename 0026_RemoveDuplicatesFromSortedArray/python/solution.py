from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       i = 0
       j = 0
       prev = -1000
       for i in range(len(nums)):
            if nums[i] != prev:
               nums[j] = nums[i]
               j += 1
               prev = nums[i]   
       return j


def main(nums):
    print(f'nums={nums}')
    ret = Solution().removeDuplicates(nums)
    print(f'Output: {ret}, {nums}')

if __name__ == "__main__":
    #nums = [1,1,2]
    #nums = [0,0,1,1,1,2,2,3,3,4]
    #nums = [100]
    #nums = [1, 1, 1]
    nums = [1, 2, 3]

    main(nums)