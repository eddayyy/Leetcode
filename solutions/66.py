class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0: return []

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0 
            
            else:
                digits[i] += 1 
                return digits

        digits.insert(0, 1)
        return digits