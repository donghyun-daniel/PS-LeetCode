class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        prereqs = [0] * n
        for prev, next in relations:
            prereqs[next - 1] |= 1 << (prev - 1)
        
        memo = {}
        
        def dfs(mask):
            if mask == (1 << n) - 1:
                return 0
            
            if mask in memo:
                return memo[mask]
            
            available = 0
            for i in range(n):
                if not (mask & (1 << i)) and (mask & prereqs[i]) == prereqs[i]:
                    available |= 1 << i
            
            if bin(available).count('1') <= k:
                result = 1 + dfs(mask | available)
            else:
                result = 9999999999
                subset = available
                while subset:
                    if bin(subset).count('1') <= k:
                        result = min(result, 1 + dfs(mask | subset))
                    subset = (subset - 1) & available
            
            memo[mask] = result
            return result

        return dfs(0)