from typing import List
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        s = ''
        queue = deque()
        queue.append(self)
        while queue:
            x = queue.popleft()
            
            if x is not None:
                s += str(x.val)
                s += ','
                queue.append(x.left)
                queue.append(x.right)
            else:
                s += 'None,'
        return s

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        N = len(nums)
        queue = deque()
        mid = N // 2
        root = TreeNode(val = nums[mid])
        if 0 < mid:
            queue.append((root, True, 0, mid))
        if mid+1 < N:
            queue.append((root, False, mid+1, N))
        while queue:
            parent, is_left, start, end = queue.popleft()
            mid = (start + end) // 2
            subroot = TreeNode(val = nums[mid])
            if is_left:
                parent.left = subroot
            else:
                parent.right = subroot
            if start < mid:
                queue.append((subroot, True, start, mid))
            if mid+1< end:
                queue.append((subroot, False, mid+1, end))
        
        return root
            

def main(nums):
    print(f'nums={nums}')
    ret = Solution().sortedArrayToBST(nums)
    print(f'Output: {ret}')




if __name__ == "__main__":
    #nums = [-10,-3,0,5,9]
    #nums = [1,3]
    #nums = [123]
    nums = [0,1,2,3,4,5,6]

    main(nums)