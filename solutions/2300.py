# Binary Search Implementation 
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        if not spells or not potions or not success: return -1 

        potions.sort()
        n, m, res = len(spells), len(potions), [] 

        for s in spells:
            left, right, idx = 0, m - 1, m

            while left <= right:
                mid = left + (right - left) // 2

                if s * potions[mid] >= success:
                    right = mid - 1
                    idx = mid 
                else:
                    left = mid + 1 

            res.append(m - idx)
                      
        return res 