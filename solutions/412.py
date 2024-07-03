class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            ans = str(i)  
            if i % 3 == 0 and i % 5 == 0: 
                ans = "FizzBuzz"
            elif i % 3 == 0:
                ans = "Fizz"
            elif i % 5 == 0: 
                ans = "Buzz"
            answer.append(ans) 
        return answer 