class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s and not wordDict: return True
        
        n = len(s)
        dp = [False] * (n + 1) 
        dp[n] = True

        print(f'S = {s} -> len(s) = {len(s)}')
        for i in range(n - 1, -1, -1):
            print(f'Entering index {i}\'s iteration:')
            for w in wordDict:
                print(f'Word is currently: {w}')
                if (i + len(w)) <= n and s[i : i + len(w)] == w:
                    print(f"Found word: {w} -> i + len(w) index = {i + len(w)} -> dp[i + len(w)] = {dp[i + len(w)]}")
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
                print(f'Iteration ending, word = {w}')
        print(dp)
        return dp[0]