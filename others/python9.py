class Solution(object):
    def maxArea(self, s):
        height = 0
        ram = 0
        left = 0
        right = len(s)-1
        while right>left :
            if s[left] >= s[right] :
                height = (right-left)*s[right]
                height = max(height, ram)
                ram = height
                right -= 1
            else :
                height = s[left]*(right-left)
                height = max(height, ram)
                ram = height
                left += 1
        return height
            