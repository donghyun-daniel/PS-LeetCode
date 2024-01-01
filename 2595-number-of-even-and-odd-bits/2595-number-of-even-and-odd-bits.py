class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0,0]
        flag = False
        while n:
            val = n & 1
            n >>= 1
            ans[flag] += val
            flag = not flag
        return ans