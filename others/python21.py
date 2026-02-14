class Solution : 
    def twoSum(self, nums, target) :
        for i in range(len(nums)) :
            for j in range(i, len(nums))  :
                if nums[i]+nums[j] == target :
                    print([i, j])
                else :
                    continue
solution = Solution()
print(solution.twoSum([2,7,11,15,1,8,1], 9))