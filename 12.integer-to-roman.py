#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L' , 90:'XC' , 100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        print(symbol) 
        i = len(symbol)-1
        while(num !=0):
            for keys in symbol.keys():
                if
                
# @lc code=end


symbol = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L' , 90:'XC' , 100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
print(symbol[0])
print(symbol) 
