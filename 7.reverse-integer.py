#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)  
        while x > 0:
         digit = x % 10        
         rev = rev * 10 + digit  
         x = x // 10           
        rev = rev * sign   

        if rev < -2**31 or rev > 2**31 - 1:
            rev = 0
            return 0
        else:
            return rev
            
        
# @lc code=end

