from collections import deque

class Solution:
    # Use dictionary to speed it up
    def isValid(self, s: str) -> bool:
        b_map = {'(':')', '{':'}', '[':']'}
        stack = deque()

        for b in s:
            v = b_map.get(b)
            if v is not None:
                # Put Closing Bracket into Stack to make the later check easier.
                stack.append(v)
                continue

            if len(stack) == 0:
                return False
            
            p = stack.pop()
            if p != b:
                return False
            
        if len(stack) != 0:
            return False
        
        return True


    def isValid(self, s: str) -> bool:
        lst = list(s)
        stack = deque()
        for b in lst:
            if b=='(' or b=='{' or b=='[':
               stack.append(b)
               continue
        
            if len(stack) == 0:
                return False
            
            p = stack.pop()
            match p:
                case '(':
                    if b != ')':
                        return False
                case '{':
                    if b != '}':
                        return False
                case _:
                    if b != ']':
                        return False
        
        if len(stack) != 0:
            return False
        
        return True


def main(s):
    print(f'Input: s = {s}')
    ret = Solution().isValid(s)
    print(f'Output: {ret}')

if __name__ == "__main__":
    #s = "()"
    #s = "()[]{}"
    #s = "(]"
    s = "([{{}}])"
    #s = "]"
 
    main(s)