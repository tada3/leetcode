from typing import List
from typing import Optional
from collections import deque
import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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
    
    # Level change can be handled by using the inner for loop.
    # Rounding down is not necessary. "Answers within 10-5 of the actual answer will be accepted." 
    # means how they check your answer.
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avg_list = []
        queue = deque()
        queue.append(root)
        while queue:
            qlen = len(queue)
            sum = 0
            for _ in range(qlen):
                node = queue.popleft()
                #print(f'node={node.val}, level={level}')
                sum += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            avg_list.append(sum, qlen)
        return avg_list
    
    @staticmethod
    def avg(sum, count):
        return math.floor(sum / count * 10**5) / 10**5

    def averageOfLevelsXXX(self, root: Optional[TreeNode]) -> List[float]:
        avg_list = []
        queue = deque()
        current_level = 0
        sum = 0
        count = 0
        queue.append((root, 0)) 
        while queue:
            node, level = queue.popleft()
            print(f'node={node.val}, level={level}')
            if level > current_level:
                avg_list.append(self.avg(sum, count))
                current_level = level
                sum = 0
                count = 0
            sum += node.val
            count += 1
            if node.left is not None:
                queue.append((node.left, level+1))
            if node.right is not None:
                queue.append((node.right, level+1))
        avg_list.append(self.avg(sum,count))
        return avg_list
    

def main(root):
    print(f'root={root}')
    root = gen_tree(root)
    print(f'XXX root(T) = {root}')
    ret = Solution().averageOfLevels(root)
    print(f'Output: {ret}')




if __name__ == "__main__":
    #root = [3,9,20,None,None,15,7]
    #root = [3,9,20,15,7]
    root = [3,9,20,15,7, 1]
    main(root)
