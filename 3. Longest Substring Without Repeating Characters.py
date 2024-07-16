import itertools

s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = "dvdf"
s5 = "yrumpkqjfdx"
s6 = "wslznzfxojzd"
s7 = "jbpnbwwd"

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length=0
        str_s=s
        point=0
        for i in range(len(s)+1):
            substring=str_s[point:i]
            print(substring)
            sub_set=list(set(substring))
            if len(sub_set)==len(substring):
                length=len(substring)
                if length>max_length:
                    max_length=length
            else:
                point+=1
                i=point
        return max_length
    
sol=Solution()
print(sol.lengthOfLongestSubstring(s=s7))