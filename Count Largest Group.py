class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict
        group_count = defaultdict(int)
        for i in range(1,n+1):
            digital_sum = sum(int(d) for d in str(i))
            group_count[digital_sum]+=1
        max_size = max(group_count.values())
        return sum(1 for count in group_count.values() if count ==max_size)
