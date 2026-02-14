class Solution(object):
    def longestCommonPrefix(self, s):
        if len(s) == 0 :
            return ""
        if len(s) == 1 :
            return s[0]
        z = []
        for i in s :
            for j in range(1, len(i)) :
                z.append(i[0:j+1])
        longest = ""
        amount = 0
        for k in z :
            if z.count(k) > amount and len(k) > len(longest) :
                longest = k
                amount = z.count(k)
        if amount>1 :
            return longest
        else :
            return ""
        
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))