class Solution(object):
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1] :
            return True
        else :
            return False
solution = Solution()
print(solution.isPalindrome(1231))