class Solution:
    def guessNumber(self, n: int) -> int:
        low, mid, high, = 1, n // 2, n 
        while low <= high:
            mid = low + (high - low) // 2
            status = guess(mid) 
            if status == 0:
                return mid
            elif status == -1:
                high = mid - 1 
            else:
                low = mid + 1 
        return -1 