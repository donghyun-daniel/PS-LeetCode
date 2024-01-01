class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        for letter in s:
            if letter=='*':
                ans.pop()
            else:
                ans+=[letter]
        return "".join(ans)