from typing import List

class Solution:        
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        l = len(nums)
        diff_a_min = 10**4 * 2
        sum_min = 0
        nums.sort()
        for i in range(0, l-2):
            j = i + 1
            k = l - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                diff =  sum - target
                if diff == 0:
                    return sum
                
                diff_a = diff * -1 if diff < 0 else diff
                if diff_a < diff_a_min:
                    diff_a_min = diff_a
                    sum_min = sum 
                
                if sum < target:
                    j += 1
                else:
                    k -= 1
        return sum_min
 

def main(nums, target):
    print(f'nums={nums}, target={target}')
    ret = Solution().threeSumClosest(nums, target)
    print(f'answer: {ret}')

if __name__ == "__main__":
    # nums = [-1,2,1,-4]
    #target = 1
    #main(nums = [0,0,0], target = 1)

    nums = [40,-53,36,89,-38,-51,80,11,-10,76,-30,46,-39,-15,4,72,83,-25,33,-69,-73,-100,-23,-37,-13,-62,-26,-54,36,-84,-65,-51,11,98,-21,49,51,78,-58,-40,95,-81,41,-17,-70,83,-88,-14,-75,-10,-44,-21,6,68,-81,-1,41,-61,-82,-24,45,19,6,-98,11,9,-66,50,-97,-2,58,17,51,-13,88,-16,-77,31,35,98,-2,0,-70,6,-34,-8,78,22,-1,-93,-39,-88,-77,-65,80,91,35,-15,7,-37,-96,65,3,33,-22,60,1,76,-32,22]
    target = 292

    main(nums, target)




