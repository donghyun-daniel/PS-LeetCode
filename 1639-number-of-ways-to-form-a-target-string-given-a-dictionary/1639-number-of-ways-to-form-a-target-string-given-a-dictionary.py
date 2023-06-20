class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(words[0])
        m = len(target)
        dp = [0] * (m+1)
        dp[0] = 1
        
        cnt = [[0] * 26 for _ in range(n)]
        for idx in range(n):
            for word in words:
                cnt[idx][ord(word[idx]) - ord('a')] += 1
        
        for idx in range(n):
            for compare in range(m-1, -1, -1):
                dp[compare+1] += dp[compare] * cnt[idx][ord(target[compare]) - ord('a')]
                dp[compare+1] %= 10**9 + 7
        
        return dp[m]