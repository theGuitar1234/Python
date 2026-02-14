import sys

class Solution(object):
    def reverse(self, s):
        if (s%10 == 0) :
            s = s//10
        if (s<0) :
            s = s*(-1)
            s = -int(str(s)[::-1])
        else :
            s = int(str(s)[::-1])
        if (s > 2**31 or s < -2**31-1) :
            return 0
        else :
            return s

solution = Solution()
print(solution.reverse(-1230))