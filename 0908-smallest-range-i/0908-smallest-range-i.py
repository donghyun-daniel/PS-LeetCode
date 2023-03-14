class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_, max_ = min(nums) + k , max(nums) - k
        return max_ - min_ if max_ > min_ else 0