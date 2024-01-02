

class Solution:
    @staticmethod
    def check_mz(ch, count, mz):
        # bin search
        ok = 0
        ng = len(mz)
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if mz[mid] <= ch:
                ok = mid
            else:
                ng = mid
        
        if mz[ok] != ch:
            return False
        
        if count == 1:
            return True
        
        count -= 1
        i = ok - 1
        while i >= 0 and mz[i] == ch:
            count -= 1
            if count == 0:
                return True
            i -= 1

        return False
        

    # Assume in operator is O(N).
    # N * M
    # But in LeetCode, canCostruct0 is around 70ms and this is 60ms. 
    # This make the magazine shorter in each step. Althouhg it take time to remove some elementes, it
    # might lead to the shorter computing time in total..
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for x in ransomNote:
            if x not in magazine:
                return False
            magazine = magazine.replace(x, '', 1)
        return True

    
    # NlogN + MlogM + N * logM
    def canConstruct0(self, ransomNote: str, magazine: str) -> bool:
        N = len(ransomNote)
        rn_sorted = sorted(ransomNote)
        M = len(magazine)
        mz_sorted = sorted(magazine)

        if rn_sorted[0] < mz_sorted[0] or mz_sorted[M-1] < rn_sorted[N-1]:
            return False

        i = 0
        while i<N:
            ch = rn_sorted[i]
            j = i + 1
            while j<N and rn_sorted[j] == ch:
                j += 1
            
            count = j - i
            if not self.check_mz(ch, count, mz_sorted):
                return False
            i = j
        
        return True
    

def main(ransomNote, magazine):
    print(f'Input: ransomNote = {ransomNote}, magazine = {magazine}')
    ret = Solution().canConstruct(ransomNote, magazine)
    print(f'Output: {ret}')




if __name__ == "__main__":
    #ransomNote = "a"
    #magazine = "b"
    #ransomNote = "aa"
    #magazine = "ab"
    #ransomNote = "aa"
    #magazine = "aab"

    ransomNote = "affc"
    magazine = "ccaabfffg"

  
    main(ransomNote, magazine)