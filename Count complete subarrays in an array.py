class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total = len(set(nums))
        n = len(nums)
        ans = 0
        for i in range(n):
            freq = set()
            for j in range(i,n):
                freq.add(nums[j])
                if len(freq) ==total:
                    ans +=1
        return ans
