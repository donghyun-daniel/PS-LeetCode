class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_val, max_val = min(nums) + k , max(nums) - k
        return max_val - min_val if max_val > min_val else 0