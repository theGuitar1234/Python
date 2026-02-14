class Solution :
    def lengthOfLongestSubstring(self, s) :
        if len(s)==1 :
            return 1
        if len(s)==0 :
            return 0
        
        left = right = 0
        longest = ""
        current = ""

        

        while right<len(s)+1 :
            for i in s[left:right+1] :
                if i in current :
                    left = right
                    if len(current) > len(longest) :
                        longest = current
                    current = ""
                    break
                current += i
            right += len(longest)+1
        if len(current) < len(longest) :
            return len(longest)
        else :
            return len(current)
        
solution = Solution()
print(solution.lengthOfLongestSubstring("pwwke"))