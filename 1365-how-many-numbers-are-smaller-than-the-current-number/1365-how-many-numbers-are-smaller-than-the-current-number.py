class Solution:
    def smallerNumbersThanCurrent(
        self, nums: List[int]
    ) -> List[int]:
        smaller_dict = {}
        for idx, num in enumerate(sorted(nums)):
            if num not in smaller_dict:
                smaller_dict[num] = idx
        return [smaller_dict[num] for num in nums]
            
        
            
            
        