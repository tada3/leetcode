from typing import List

class Solution:
    @classmethod
    def mergesort(cls, src1, src1Start, src1End, src2, src2Start, src2End, dest, destStart, destEnd):
        i = src1Start
        j = src2Start
        p = destStart
        while p < destEnd:
            if i == src1End:
                if j == src2End:
                    break
                else:
                    dest[p] = src2[j]
                    j += 1
            else:
                if j == src2End:
                    dest[p] = src1[i]
                    i += 1
                else:
                    if src1[i] < src2[j]:
                        dest[p] = src1[i]
                        i += 1
                    else:
                        dest[p] = src2[j]
                        j += 1
            p += 1
        return i, j


    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            # do nothing
            return

        if m == 0:
            nums1[:] = nums2[:]
            return

        if m <= n:
            # This does not work when m==0
            nums1[-m:] = nums1[:m]

            self.mergesort(nums1, -m, 0, nums2, 0, n, nums1, 0, m+n)
            return
        
        i = 0
        while True:
            if i >= m - n:
                # last block, can be smaller than n
                size = min(m-i, n)
                nums1[-size:] = nums1[i:i+size]
                self.mergesort(nums1, -size, 0, nums2, 0, n, nums1, i, m+n)
                break
            else:
                nums1[-n:] = nums1[i:i+n]
                p, q = self.mergesort(nums1, -n, 0, nums2, 0, n, nums1, i, i+n)
                self.mergesort(nums1, p, 0, nums2, q, n, nums2, 0, n)
                i += n
            



def main(nums1, m, nums2, n):
    print(f'nums1={nums1}, m={m}, nums2={nums2}, n={n}')
    Solution().merge(nums1, m, nums2, n)
    print(f'answer: {nums1}')

if __name__ == "__main__":
    #nums1=[1,3]
    #nums1 = [1,2,3,0,0,0]
    #m = 3
    #nums2 = [2,5,6]
    #n = 3

    # nums1 = [1]
    # m = 1
    # nums2 = []
    # n = 0

    # nums1 = [0]
    # m = 0
    # nums2 = [1]
    # n = 1

    nums1 = [1,2,4,5,6,0]
    m = 5
    nums2 = [3]
    n = 1

    main(nums1, m, nums2, n)


    

                