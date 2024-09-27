# Two Sum -II{Amazon}
# Solution-1 easy and my solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevmap ={} #val:index
        for i,n in enumerate(numbers):
            diff = target-n
            if diff in prevmap:
                return [prevmap[diff]+1,i+1]
            prevmap[n]=i
        return        

# Solution-2 easy but one test case fails

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r =0 ,len(numbers)-1 #first element, lasr element

        while l<r:
            cursum = numbers[l]+numbers[r]

            if cursum > target:
                r = r-1 #right pointer decrease
            elif cursum > target:
                l = l+1
            else:
                return [l+1, r+1]
        return []                



