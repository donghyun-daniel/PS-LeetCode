class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        nums_cnt = len(nums)
        asc_dp = [1 for _ in range(nums_cnt)]
        dsc_dp = [1 for _ in range(nums_cnt)]
        indices = []
        for idx in range(nums_cnt - 1):
            reversed_idx = nums_cnt-idx-1
            asc_dp[idx+1] = 1 if nums[idx+1] > nums[idx] else asc_dp[idx] + 1
            dsc_dp[reversed_idx-1] = 1 if nums[reversed_idx] < nums[reversed_idx-1] else dsc_dp[reversed_idx] + 1
        for idx in range(1, nums_cnt-1):
            if asc_dp[idx-1] >= k and dsc_dp[idx+1] >= k:
                indices.append(idx)
            
        return indices