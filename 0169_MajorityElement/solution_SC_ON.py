from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tab = {}
        max = 0
        max_elem = -1
        for x in nums:
            if x in tab:
                tab[x] += 1
            else:
                tab[x] = 1
            if tab[x] > max:
                max = tab[x]
                max_elem = x
    
        return max_elem

def main(nums):
    print(f'nums={nums}')
    ret = Solution().majorityElement(nums)
    print(f'Output: {ret}')

if __name__ == "__main__":
    #nums = [3,2,3]
    nums = [2,2,1,1,1,2,2]

    main(nums)