from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ok = 0
        ng = len(nums)

        if nums[ok] > target:
            return 0

        while ng - ok > 1:
            print(f'ok={ok}, ng={ng}')
            mid = (ok + ng) // 2
            if nums[mid] <= target:
                ok = mid
            else:
                ng = mid
        
        if nums[ok] == target:
            return ok
        return ok + 1

def main(nums, target):
    print(f'nums = {nums}, target = {target}')
    ret = Solution().searchInsert(nums, target)
    print(f'Output: {ret}')

if __name__ == "__main__":
    #nums = [1,3,5,6]
    #target = 5
    #nums = [1,3,5,6]
    #target = 7
    #nums = [2]
    #target = 3
    nums = [2, 4, 5]
    target = -1
    nums = [2]
    target = -1

    main(nums, target)

