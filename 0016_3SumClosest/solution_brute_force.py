from typing import List

class Solution:
    def getNewVals(self, sum, target, diff_min, ret):
        d = sum - target
        if d < 0:
            d *= -1
        if d < diff_min:
            diff_min = d
            ret = sum
        return diff_min, ret
        
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        l = len(nums)
        diff_min = 2 * 10**4
        ret = 0
        for a in range(0, l-2):
            for b in range(a+1, l-1):
                for c in range(b+1, l):
                    sum = nums[a] + nums[b] + nums[c]
                    diff_min, ret = self.getNewVals(sum, target, diff_min, ret)
        return ret
 

def main(nums, target):
    print(f'nums={nums}, target={target}')
    ret = Solution().threeSumClosest(nums, target)
    print(f'answer: {ret}')

if __name__ == "__main__":
    #main(nums = [-1,2,1,-4], target = 1)
    main(nums = [0,0,0], target = 1)



