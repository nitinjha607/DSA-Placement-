# My approach 26 /100 testcase passed
class Solution:
    def isValid(self, s: str) -> bool:
        count1 = 0
        count2 = 0
        s = input()
        for i in s:
            if i =="(":
                count1 +=1
            elif i ==")":
                count2 +=1 
            if i =="{":
                count1 +=1
            elif i =="}":
                count2 +=1
            if i =="[":
                count1 +=1
            elif i =="]":
                count2 +=1   
        print(count1)
        print(count2)

        if count1 == count2:
            t = True
        else:
            t = False 
        return t    

# Instructor approach
class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        closetoopen= {")":"(","]":"[","}":"{"}
        for c in s:
            if c in closetoopen:
                if stack and stack[-1] == closetoopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False                    
