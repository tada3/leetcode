from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.tail = False

    def __str__(self):
        lst = []
        ln = self
        while True:
            lst.append(ln.val)
            if ln.tail:
                break
            ln = ln.next
        return str(lst)


def gen_list(head, pos):
    if len(head) == 0:
        return None
    
    root = ListNode(head[0])
    prev = root
    for v in head[1:]:
        ln = ListNode(v)
        prev.next = ln
        prev = ln

    tail = prev
    tail.tail = True

    if pos < 0:
        return root
    
    cn = root
    for _ in range(pos):
        cn = cn.next
    tail.next = cn 

    return root  


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        kame = head
        usagi = head
        while usagi.next is not None and usagi.next.next is not None:
            kame = kame.next
            usagi = usagi.next.next
            if usagi == kame:
                return True
            
        return False

def main(head, pos):
    print(f'Input: head = {head}, pos = {pos}')
    head = gen_list(head, pos)
    print(f'XXX head(List)) = {head}')
    ret = Solution().hasCycle(head)
    print(f'Output: {ret}')

if __name__ == "__main__":
    #head = [3,2,0,-4]
    #pos = 1
    

    #head = [1]
    #pos = -1

    #head = []
    #pos = -1

    head = [3,2,0,-4]
    pos = -1
 
    main(head, pos)


