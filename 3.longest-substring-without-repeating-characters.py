#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l= 0
        store=set()
        limit=0
        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l+=1
            store.add(s[r])
            limit=max(limit,r-l+1)
        return limit




# @lc code=end

