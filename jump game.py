# Greedy approach solve this problem in O(n) time and dynammic takes O(n**2) and brute force approach takes O(n**n)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i +nums[i] >= goal:
                goal = i
        return True if goal ==0 else False
