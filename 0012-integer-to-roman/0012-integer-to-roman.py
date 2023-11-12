class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ['I', 'X', 'C', 'M']
        fives = ['V', 'L', 'D']
        idx = 0
        ans = []

        while num > 0:
            rem = num % 10
            if 1 <= rem <= 3:
                ans.append(ones[idx] * rem) 
            elif rem == 4:
                ans.append(ones[idx] + fives[idx])
            elif 5 <= rem <= 8:
                ans.append(fives[idx] + ones[idx] * (rem - 5))
            elif rem == 9:
                ans.append(ones[idx] + ones[idx+1])
            idx += 1
            num //= 10

        return "".join(ans[::-1])