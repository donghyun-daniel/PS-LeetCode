class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights: return 0
        
        l_max, r_max = 0, 0
        l, r = 0, len(heights) - 1
        
        water = 0
        while l < r:
            if heights[l] < heights[r]:
                if heights[l] > l_max:
                    l_max = heights[l]
                else:
                    water += l_max - heights[l]
                l += 1
            else:
                if heights[r] > r_max:
                    r_max = heights[r]
                else:
                    water += r_max - heights[r]
                r -= 1
        
        return water