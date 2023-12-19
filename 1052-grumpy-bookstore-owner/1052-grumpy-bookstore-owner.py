class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        good_idx, alpha = 0, 0
        
        for start_idx in range(len(customers)-minutes+1):
            new_alpha = sum(
                [customers[idx] for idx in range(start_idx, start_idx+minutes) if grumpy[idx] == 1]
            )
            if alpha < new_alpha:
                alpha = new_alpha
                good_idx = start_idx

        for minute in range(minutes):
            grumpy[good_idx+minute] = 0
            
        return sum([c for c, g in zip(customers, grumpy) if g==0])
        