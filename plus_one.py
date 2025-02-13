class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n =""
        for i in digits:
            n +=str(i)
        n1 = int(n)
        n2 = n1+1
        n3 = str(n2)
        n4 = []
        for i in n3:
            n4.append(int(i))

        return n4    
