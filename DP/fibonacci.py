class Solution:
    def __init__(self):
        self.memo={}

    def fib(self, n: int) -> int:
        if n < 2 :
            return n
        if  n in self.memo:
            return self.memo[n]
        
        self.memo[n]=self.fib(n-1)+ self.fib(n-2)
        
        return self.memo[n]
    


# Example usage:
solution = Solution()
print(solution.fib(10))  # Output will be 55