#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        i =0 
        j = len(height)-1
        while i<j:
            result = max(result,(j-i)*min(height[i],height[j]))
            if(height[i] <height[j]):
                i+=1
            else :
                j-=1
        return result
                
# @lc code=end

