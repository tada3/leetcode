from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = sum_j = nums[0]
        for x in nums[1:]:
            sum_j = max(sum_j + x, x)
            if sum_j > max_sum:
                max_sum = sum_j
        return max_sum



def main(nums):
    print(f'Input: nums = {nums}')
    ret = Solution().maxSubArray(nums)
    print(f'Output: {ret}')

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [1]
    nums = [5,4,-1,7,8]
    main(nums)


