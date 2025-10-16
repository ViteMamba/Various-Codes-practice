#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        print(s)
        start = l
        end = 0
        l=0
        r=0
        for i in range (1,len(s)):
            r=i
            if(s[l]==s[r]):
                if(r-l >start-end):
                    end = r
                    s=l
                    l+=1
                    

# @lc code=end
S= Solution()
S.longestPalindrome("babad")

