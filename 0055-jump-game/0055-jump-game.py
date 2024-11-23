class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = len(nums) - 1
        for idx in range(len(nums) -2, -1, -1):
            if idx + nums[idx] >= max_reach:
                max_reach = idx
        return max_reach == 0
        