from typing import List

# Space Complexity O(1)
# Iterate on the array with the following manipulations.
# (1) count == 0 means a neutral state. Set maj to the new element and set count to 1.
# (2) if count > 0 and the new element is the same as maj, increment the count.
# (3) otherwise, decrement the count. (leave the maj as it is.)
# Why does this work?
# Consider a simple case where there are only 2 unique numbers in the array, A and B. 
# And suppose that A is the major element.
# In this case, count will be num_of_A - num_of_B and maj is A in any order. 
# If you replace some of B with other numbers, count will be greater and maj will be still be A. 
# So, we can use the above method to find the major element. 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = nums[0]
        count = 1
        for x in nums[1:]:
            if count == 0:
                count = 1
                maj = x
            elif x == maj:
                count += 1
            else:
                count -= 1
        return maj

def main(nums):
    print(f'nums={nums}')
    ret = Solution().majorityElement(nums)
    print(f'Output: {ret}')

if __name__ == "__main__":
    #nums = [3,2,3]
    #nums = [2,2,1,1,1,2,2]
    nums = [3]

    main(nums)