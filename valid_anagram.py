# Valid Anagram 
#Solution-1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a =[]
        b =[]
        for i in s:
            a.append(i)
        for j in t:
            b.append(j)
        a.sort()
        b.sort()
        if a == b:
            return True
        else:
            return False        

#Solution-2(Good Solution)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT= {}, {}

        for i in range(len(s)):
            countS[s[i]] =1 + countS.get(s[i],0)
            countT[t[i]] =1 + countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False 
        return True           
               
        
        
