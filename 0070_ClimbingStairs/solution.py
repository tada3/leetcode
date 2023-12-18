from typing import List

# DP(n+1) = DP(n) + DP(n-1)
# Let DP(n) be the distinct ways to climb to the n+1 th staircase.
# There are two ways to climb to the n+1 th staircase.
#  (1) Go to the n th staircase and climb 1 step to the n+1 th staircase.
#  (2) Go to the n-1 th staircase and climb 2 steps to the n+1 th staircase.
#      Note that you do not stop at the n th staircase.
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

def main(n):
    print(f'n={n}')
    ret = Solution().climbStairs(n)
    print(f'Output: {ret}')

if __name__ == "__main__":
    #n = 2 
    #n = 3
    n = 9
    
    main(n)