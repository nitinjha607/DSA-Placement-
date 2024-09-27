# House Robber {Google}
# Solution-1 Easy and my solution but some test case fails
class Solution:
    def rob(self, nums: List[int]) -> int:
        sum1 =0
        sumodd =0
        sumeven =0
        for i,n in enumerate(nums):
            if i%2 ==0:
                sumeven +=n
            if i%2 !=0:
                sumodd +=n 
        if sumodd > sumeven :
            sum1 = sumodd
        else:
            sum1 = sumeven
        return sum1                    
# Solution-2 Easy and optimized solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0 
        # [rob1, rob2, n, n+1,...]

        for n in nums:
            temp = max(n +rob1, rob2)
            rob1= rob2
            rob2 =temp
        return rob2    


        
