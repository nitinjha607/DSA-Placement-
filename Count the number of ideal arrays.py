class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        from math import comb
        MOD = 10**9 + 7

        # Precompute the divisors
        divisors = [[] for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1):
            for j in range(i * 2, maxValue + 1, i):
                divisors[j].append(i)

        # dp[i][k] will store number of sequences of length k ending at i
        maxLen = min(n, 14)  # max needed length for combinations
        dp = [[0] * (maxLen + 1) for _ in range(maxValue + 1)]

        for i in range(1, maxValue + 1):
            dp[i][1] = 1

        for length in range(2, maxLen + 1):
            for i in range(1, maxValue + 1):
                for d in divisors[i]:
                    dp[i][length] += dp[d][length - 1]
                    dp[i][length] %= MOD

        res = 0
        for length in range(1, maxLen + 1):
            count = comb(n - 1, length - 1)
            for i in range(1, maxValue + 1):
                res = (res + count * dp[i][length]) % MOD

        return res
