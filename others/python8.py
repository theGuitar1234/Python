class Solution(object):
    def isMatch(self, s, p):
        z = list(s)
        k = list(p)
        n = 0
        o = 0
        for i in z :
            for j in k :
                if j=="." :
                    z[n] = ""
                    k[n] = ""
                    n +=1
                else : 
                    continue
        if z==k :
            return True
        else :
            return False
solution = Solution()
print(solution.isMatch("aab", "a.."))