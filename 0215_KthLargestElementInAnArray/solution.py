from typing import List



# Use Heap
#            0                   1
#        1       2               2
#      3   4   5   6             4
#    7   8                       8
""" 
a[i] = 2^i
S[n] = 1 + 2 + ... 2^n
2S[n] =    2 + ... 2^2 + 2^n+1
S[n] = 2^n+1 -1

Layer iの最後は  2^i+1 -1 -1 = 2^i+1 - 2
Layer iの最初は Layer i-1 の最後 + 1 = 2^i - 2 + 1 = 2^i - 1
よって

Layer i: [2^i - 1, 2^i+1 - 2]
Layer i+1: [2^i+1 -1, 2^i+2 - 2]
Kの親: (K-1)//2
Kの左子: 2K +1
Kの右子 2K + 2
 """




class Solution:
    @staticmethod
    def heapify(array, i, size):
        lc = 2 * i + 1
        rc = lc + 1
        largest = i
        if lc < size and array[lc] > array[i]:
            largest = lc
        if rc < size and array[rc] > array[largest]:
            largest = rc
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            Solution.heapify(array, largest, size)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # build heap
        start = (n-1-1)//2
        for i in range(start, -1, -1):
            self.heapify(nums, i, n)

        # swap and rebuild
        for i in range(k-1):
            nums[0] = nums[n-1-i]
            self.heapify(nums, 0, n-1-i)

        return nums[0]
    


def main(nums, k):
    print(f'Input: nums = {nums}, k = {k}')
    ret = Solution().findKthLargest(nums, k)
    print(f'Output: {ret}')




if __name__ == "__main__":
    #nums = [3,2,1,5,6,4]
    #k = 2

    nums = [3,2,3,1,2,4,5,5,6]
    k = 4


    main(nums, k)