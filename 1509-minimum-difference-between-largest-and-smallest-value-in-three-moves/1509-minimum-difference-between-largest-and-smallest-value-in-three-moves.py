class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums = sorted(nums)
        return min([nums[-i] - nums[4-i] for i in range(1, 5)])
        