class Solution:
    def minSteps(self, s: str, t: str) -> int:
        tCount, sCount = Counter(t), Counter(s)

        res = 0

        for key, val in sCount.items():
            if key in tCount:
                res += max(0, val - tCount[key])
            else:
                res += val

        return res 