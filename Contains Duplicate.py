# Method-1 My method
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num1 = set(nums)
        x = len(nums) - len(num1)
        if x != 0:
            return True
        else:
            return False    

# Method -2 Instructor Method
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
