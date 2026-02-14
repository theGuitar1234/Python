class Solution(object):
    def threeSum(self, nums):
        z = []
        t = []
        n = 0

        for i in nums :
            n+=1
            for j in nums[n:] :
                for l in nums[n+1:] :
                    if j+l == -i :
                        z = [i, j, l]
                        z.sort()
                        t.append(z)
        for i in t :
            for j in t[1:] :
                if i == j :
                    t.remove(j)
        return t

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))

