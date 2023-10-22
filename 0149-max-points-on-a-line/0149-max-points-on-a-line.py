class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def get_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1==x2:
                return inf
            return (y1-y2)/(x1-x2)
        
        if len(points) <= 2:
            return len(points)
        
        ans = 1
        
        for idx_1, p1 in enumerate(points):
            slopes = defaultdict(int)
            for idx_2, p2 in enumerate(points[idx_1+1:]):
                slope = get_slope(p1, p2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans+1