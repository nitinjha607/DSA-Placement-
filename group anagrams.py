from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26  # 26 lowercase English letters
            for c in s:
                count[ord(c) - ord("a")] += 1  # ✅ increment the correct index
            res[tuple(count)].append(s)  # tuple used as key because lists can't be keys

        return list(res.values())  # ✅ convert to list before returning
