class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)
        result = 0
        idx = 0
        
        for house in houses:
            while idx + 1 < len(heaters) and heaters[idx+1] == heaters[idx]:
                idx += 1
            while idx + 1 < len(heaters) and abs(heaters[idx+1] - house) < abs(heaters[idx] - house):
                idx += 1
            result = max(result, abs(heaters[idx] - house))
        return result