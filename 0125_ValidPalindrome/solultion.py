class Solution:
    def isPalindrome(self, s: str) -> bool:           
        s = s.replace(' ', '').lower()
        i = 0
        j = len(s) - 1
        while i<j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

def main(s):
    print(f'Input: s = {s}')
    ret = Solution().isPalindrome(s)
    print(f'Output: {ret}')


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    s = "0P"
  
    main(s)