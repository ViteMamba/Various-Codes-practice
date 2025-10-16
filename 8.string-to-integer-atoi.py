#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        l = 0
        r= 0
        length=0
        f=0
        number=""
        i = 0
        sign = 1
        low = -2**31
        high = (2**31)-1
        while i<len(s) and s[i]==" ":
            i+=1
        
        if  i == len(s):
            return 0
        print(i)
        if s[i] == "+":
            i+=1
            pass
        elif s[i] == "-":
            sign = -1
            i+=1
        res = 0
        while i< len(s) and s[i].isdigit():
            digit = int(s[i])
            res = res*10 + digit
            
            if sign* res <= low:
                return low
            if sign*res>=high:
                return high
            i+=1
        res = res*sign
        return res
                
# @lc code=end

