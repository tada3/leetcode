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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Traverse the tree inorder
        stack = deque()
        node = root
        min_diff = 10**6
        prev = -10**6
        while True:
#            print(f'XXX node = {node.val}')
            if node.left is not None:
                # (a) left exists
                tmp = node.left
                node.left = None
                stack.append(node)
                node = tmp
                continue

            diff = node.val - prev
            if diff < min_diff:
                if diff == 1:
                    return 1
                min_diff = diff
            prev = node.val
            if node.right is not None:
                # (b) left does not exist, but right exists
                node = node.right
                continue

            # (c) Neither left nor right exists
            if not stack:
                return min_diff
            node = stack.pop()
                
def main(root):
    print(f'Input: {root}')
    t = gen_tree(root)
    print(f'tree = {t}')
    ret = Solution().getMinimumDifference(t)
    print(f'Output: {ret}')




if __name__ == "__main__":
    #root = [4,2,6,1,3]
    root = [1,0,48,None,None,12,49]



    main(root)