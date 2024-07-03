class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return n 
        first, second = 1, 1 

        for i in range(n):
            temp = first + second
            print(f'i: {i}, temp: {temp}, first: {first}, second: {second}')
            first = second
            second = temp
            print(f'END: i: {i}, temp: {temp}, first: {first}, second: {second}')
        return first