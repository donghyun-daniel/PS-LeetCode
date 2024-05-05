class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(nums, key=lambda x: x/(10 ** len(str(x)) - 1), reverse=True)
        return str(int(''.join([str(num) for num in nums])))