class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0,0]
        cnt = 0
        while n:
            val = n & 1
            n >>= 1
            ans[cnt] += val
            cnt = (cnt + 1) % 2
        return ans