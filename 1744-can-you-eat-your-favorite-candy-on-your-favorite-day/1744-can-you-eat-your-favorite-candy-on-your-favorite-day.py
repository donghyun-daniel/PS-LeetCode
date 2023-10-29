class Solution:
    def canEat(self, candies_count: List[int], queries: List[List[int]]) -> List[bool]:
        acc_candies = [0] + list(accumulate(candies_count))
        return [
            d - candies_count[t] < acc_candies[t] < c * (d + 1) 
            for t, d, c in queries
        ]