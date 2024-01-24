from typing import List
from typing import Optional
from collections import deque



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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

def gen_tree(nums):
    if len(nums) == 0:
        return None
    queue = deque()
    root = TreeNode(nums[0])
    idx = 1
    if idx < len(nums):
        v = nums[idx]
        if v is not None:
            queue.append((root, True, v))
        idx += 1
    if idx < len(nums):
        v = nums[idx]
        if v is not None:
            queue.append((root, False, v))
        idx += 1
    while queue:
        parent, is_left, v = queue.popleft()
        node = TreeNode(v)
        if is_left:
            parent.left = node
        else:
            parent.right = node
        if idx < len(nums):
            v = nums[idx]
            if v is not None:
                queue.append((node, True, v))
            idx += 1
        if idx < len(nums):
            v = nums[idx]
            if v is not None:
                queue.append((node, False, v))
            idx += 1
    return root
    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        max_depth = 0
        stack = deque()
        stack.append((1, root))
        while stack:
            depth, node = stack.pop()
            if depth > max_depth:
                max_depth = depth
            if node.left is not None:
                stack.append((depth+1, node.left))          
            if node.right is not None:
                stack.append((depth+1,node.right))
        return max_depth
    


def main(root):
    print(f'Input: {root}')
    t = gen_tree(root)
    ret = Solution().maxDepth(t)
    print(f'Output: {ret}')




if __name__ == "__main__":
    root = [3,9,20,None,None,15,7]
    root = [1,None,2]
    root = []
    root = [-100]
 
    main(root)