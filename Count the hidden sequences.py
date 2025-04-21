class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for d in differences:
            prefix.append(prefix[-1]+d)
        min_prefix = min(prefix)
        max_prefix = max(prefix)

        min_x = lower -min_prefix
        max_x = upper -max_prefix
        ans = max(0,max_x-min_x+1)
        return ans 
