class Solution(object):
    def myAtoi(self, s):
        s = s.strip()

        if s=="" :
            return 0
        
        t = ""
        sign = 1

        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        
        for i in s :
            if i.isdigit() :
                t = t+i
            else :
                break
        
        if t=="" :
            return 0
        
        num = int(t)*sign

        if num < -2**31 :
            return -2**31
        if num > 2**31-1:
            return 2**31-1
        return num
        
solution = Solution()
print(solution.myAtoi("+-1"))