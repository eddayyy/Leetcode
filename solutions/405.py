class Solution:
    def toHex(self, num: int) -> str:
        if not num: return '0'

        if num < 0:
            num = (1 << 32) + num

        hex_digits = '0123456789abcdef'

        hex_rep = ''

        while num > 0: 
            digit = num % 16
            hex_dig = hex_digits[digit] 
            hex_rep = hex_dig + hex_rep 
            num = num // 16 
        
        return hex_rep 