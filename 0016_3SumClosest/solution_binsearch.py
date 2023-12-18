from typing import List

class Solution:
    
    @classmethod
    def get_diff(cls, c, a, b, target):
        sum = c + a + b
        d =  sum - target
        if d < 0:
            d *= -1
            return sum, d, -1
        return sum, d, d
    
    @classmethod
    def bin_search0(cls, start, end, nums, a, b, target):
        sum0 = a + b
        if sum0 + nums[start] >=0 or sum0 + nums[end-1] <= 0:
            return cls.bin_search2(start, end, nums, a, b, target)
        
        p = cls.bin_search1(start, end, sum0, nums)
        s1, d1 = cls.bin_search2(start, p, nums, a, b, target)
        s2, d2 = cls.bin_search2(p, end, nums, a, b, target)
        if d1 < d2:
            return s1, d1
        return s2, d2

    @classmethod
    def bin_search1(cls, start, end, sum0, nums):
        if end - start == 1:
            return start
        mid = (start + end) // 2
        check = sum0 + nums[mid]
        if check <= 0:
            return cls.bin_search1(mid, end, sum0, nums)
        return cls.bin_search1(start, mid, sum0, nums)


    @classmethod
    def bin_search2(cls, start, end, nums, a, b, target):
        if end - start <= 2:
            if end - start == 1:
                s, d, _ = cls.get_diff(nums[start], a, b, target)
                return s, d
            sum_start, d_start, _ = cls.get_diff(nums[start], a, b, target)
            sum_end, d_end, _ = cls.get_diff(nums[end-1], a, b, target)
            if d_start < d_end:
                return sum_start, d_start
            return sum_end, d_end

        mid = (start + end) // 2
        s, _, f = cls.get_diff(nums[mid], a, b, target)
        if f == 0:
            return s, 0
        if f < 0:
            return cls.bin_search2(mid, end, nums, a, b, target)
        return cls.bin_search2(start, mid+1, nums, a, b, target)


        
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        l = len(nums)
        diff_min = 2 * 10**4
        sum_min = 0
        nums.sort()
        for i in range(0, l-2):
            for j in range(i+1, l-1):
                sum, diff = self.bin_search0(j+1, l, nums, nums[i], nums[j], target)
                if diff < diff_min:
                    diff_min = diff
                    sum_min = sum
        return sum_min
 

def main(nums, target):
    print(f'nums={nums}, target={target}')
    ret = Solution().threeSumClosest(nums, target)
    print(f'answer: {ret}')

if __name__ == "__main__":
    #main(nums = [-1,2,1,-4], target = 1)
    #main(nums = [0,0,0], target = 1)

    nums = [40,-53,36,89,-38,-51,80,11,-10,76,-30,46,-39,-15,4,72,83,-25,33,-69,-73,-100,-23,-37,-13,-62,-26,-54,36,-84,-65,-51,11,98,-21,49,51,78,-58,-40,95,-81,41,-17,-70,83,-88,-14,-75,-10,-44,-21,6,68,-81,-1,41,-61,-82,-24,45,19,6,-98,11,9,-66,50,-97,-2,58,17,51,-13,88,-16,-77,31,35,98,-2,0,-70,6,-34,-8,78,22,-1,-93,-39,-88,-77,-65,80,91,35,-15,7,-37,-96,65,3,33,-22,60,1,76,-32,22]
    target = 292

    main(nums, target)




