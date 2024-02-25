class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        import heapq
        projects = sorted([(c, p) for c, p in zip(capital, profits)])
        h, idx, n = [], 0, len(projects)
        while k > 0 :
            while idx < n and (values := projects[idx])[0] <= w:
                heapq.heappush(h, (-values[1]))
                idx += 1
            if h:
                w -= heapq.heappop(h)
                k -= 1 
            else:
                break
        return w