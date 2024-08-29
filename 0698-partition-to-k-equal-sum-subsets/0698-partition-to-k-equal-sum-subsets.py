class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        used = [False] * len(nums)
        nums = sorted(nums, reverse=True)
        
        def backtrack(idx, cnt, curr_sum):
            if cnt == k - 1:
                return True
            if curr_sum == target:
                return backtrack(0, cnt + 1, 0)
            for i in range(idx, len(nums)):
                if used[i] or curr_sum + nums[i] > target:
                    continue
                used[i] = True
                if backtrack(i + 1, cnt, curr_sum + nums[i]):
                    return True
                used[i] = False
                if curr_sum == 0:
                    break
            return False
        return backtrack(0, 0, 0)