class Solution:
    def getMaximumXor(self, nums: List[int], max_bit: int) -> List[int]:
        result = []
        max_num = pow(2, max_bit) - 1
        tmp_xor = reduce(lambda x, y: x ^ y, nums)
        for _ in range(len(nums)):
            result.append(tmp_xor ^ max_num)
            tmp_xor ^= nums.pop()
        return result