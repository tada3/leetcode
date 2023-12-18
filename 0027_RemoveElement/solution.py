from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        i = 0
        j = l - 1
        while True:
            print('i,j', i, j)
            while i < l and nums[i] != val:
                i += 1

            while j >= 0 and nums[j] == val:
                j -= 1

            if i > j:
                break
            
            nums[i] = nums[j]
            nums[j] = val
            i += 1
            j -= 1
        return i




def main(nums, target):
    print(f'nums={nums}, val={val}')
    ret = Solution().removeElement(nums, val)
    print(f'answer: {ret}')

if __name__ == "__main__":
    #nums = [3,2,2,3]
    #val = 3

    #ums = [0,1,2,2,3,0,4,2]
    #val = 2

    #nums = []
    #val = 3

    nums = [4, 5]
    val = 4

    main(nums, val)

