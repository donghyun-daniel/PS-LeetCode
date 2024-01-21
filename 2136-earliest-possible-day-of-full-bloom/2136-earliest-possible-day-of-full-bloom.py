class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        times = list(zip(plantTime, growTime))
        times = sorted(times, key=lambda x: -x[1])
        
        result = 0
        start_time = 0
        for plant, grow in times:
            start_time += plant
            result = max(result, start_time + grow)
        return result