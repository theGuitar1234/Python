class Solution(object):
    def longestPalindrome(self, s):
        maxLen = 0
        result = ""
        while len(s)>=1 :
            z = ""
            k = ""
            for i in s :
                z = z+i
                if z == z[::-1] :
                    if len(z) > maxLen :
                        maxLen = len(z)
                        result = z
                else :
                    continue
            s = s[1:]
        return result

solution = Solution()
print(solution.longestPalindrome("baba"))