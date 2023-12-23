from collections import deque

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a
        
        c = ['0'] * len(a)
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0:
            x = carry
            bj = b[j] if j >= 0 else '0'
            if a[i] != bj:
                x += 1
            elif a[i] == '1':
                x += 2

            if x > 1:
                carry = 1
                x -= 2
            else:
                carry = 0

            c[i] = str(x)
            i -= 1
            j -= 1

        if carry > 0:
            c.insert(0, '1')
        return ''.join(c)
    

    def addBinaryStack(self, a: str, b: str) -> str:
        if len(b) > len(a):
            tmp = a
            a = b
            b = tmp
        
        stack = deque()
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0:
            x = carry
            if j >= 0:
                if a[i] != b[j]:
                    x += 1
                elif a[i] == '1':
                    x += 2
            else:
                if a[i] == '1':
                    x += 1

            if x > 1:
                carry = 1
                x -= 2
            else:
                carry = 0
            stack.append(x)
            i -= 1
            j -= 1
        if carry > 0:
            stack.append(1)

        l = []
        while stack:
            x = stack.pop()
            print(f'x = {x}')
            if x == 0:
                l.append('0')
            else:
                l.append('1')

        return ''.join(l)


def main(a, b):
    print(f'a = {a}, b = {b}')
    ret = Solution().addBinary(a, b)
    print(f'Output: {ret}')

if __name__ == "__main__":
    #a = "11"
    #b = "1"
    #a = "1010"
    #b = "1011"
    #a = "0"
    #b = "1"
    a = "100"
    b = "110010"

    main(a, b)