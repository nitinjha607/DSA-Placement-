# My Solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        return len(l[-1])

# Instructor solution falis test case
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s)-1, 0 
        while s[i] == "":
            i -= 1
        while i >= 0 and s[i] != " ":
            length +=1
            i -=1
        return length         
