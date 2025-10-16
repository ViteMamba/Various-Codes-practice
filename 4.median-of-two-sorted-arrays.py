#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        finallist = nums1+nums2
        finallist.sort()
        mid = int(len(finallist)/2)
        if len(finallist)%2!=0:
            result = float( finallist[mid])
            return result
        else:
            result = float((finallist[mid] +finallist[mid-1])/2)
            return result            
# @lc code=end

