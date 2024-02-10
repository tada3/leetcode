from collections import deque

class Solution:
    def totalNQueens(self, n: int) -> int:
        # Backtrak with stack
        count = 0
        stack = deque()
        stack.append([])
        while stack:
            x = stack.pop()
            if len(x) == n:
                count += 1
                continue
            
            next = len(x)
            check = [0] * n
            for i in range(next):
                # i -> next
                check[x[i]] = 1
                diag1 = x[i] - (next - i)
                if diag1 >= 0:
                    check[diag1] = 1
                diag2 = x[i] + (next - i) 
                if diag2 < n:
                    check[diag2] = 1
            for j in range(n):
                if check[j] == 0:
                    stack.append(x + [j])
        return count



def main(n):
    print(f'Input: n = {n}')
    ret = Solution().totalNQueens(n)
    print(f'Output: {ret}')




if __name__ == "__main__":
    n = 4
    n = 1
    main(n)