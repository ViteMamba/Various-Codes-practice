#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h={}
        for i in range (len(nums)):
            h[nums[i]]=i
        print (h)
        for i in range (len(nums)):
            y = target - nums[i]
            print(y)
            if y in h and h[y] != i:
                return [i,h[y]]
# @lc code=end
s = Solution()

print(s.twoSum([3,2,4], 6))
