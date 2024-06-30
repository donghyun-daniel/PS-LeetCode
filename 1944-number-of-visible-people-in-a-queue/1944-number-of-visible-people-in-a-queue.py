class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0] * n
        stack = []
        
        for idx in range(n - 1, -1, -1):
            while stack and heights[idx] > stack[-1]:
                stack.pop()
                answer[idx] += 1
            if stack:
                answer[idx] += 1
            
            stack.append(heights[idx])
        return answer