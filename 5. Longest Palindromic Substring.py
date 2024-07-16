s1 = "babad"
s2 = "cbbd"
s3 ="a"
s4 = "bb"
s5 = "abb"

class Solution(object):
    def longestPalindrome(self, s):
        if s==s[::-1]:
            return s
        for i in range(len(s)):
            j=0
            while True:
                string=s[j:len(s)-i+j]
                print("string: "+string)
                if string == string[::-1]:
                    return string
                if (len(s)-i+j)==len(s):
                    j=0
                    break
                j+=1

                
sol=Solution()
print(sol.longestPalindrome(s=s5))