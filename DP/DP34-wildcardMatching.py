class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l = len(s)
        k = len(p)
        
        # Memoization table
        memo = {}
        
        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base cases
            if i < 0 and j < 0:  # Both strings are exhausted
                return True
            if j < 0:  # Pattern exhausted but string is not
                return False
            if i < 0:  # String exhausted, check if remaining pattern is all '*'
                for x in range(j + 1):
                    if p[x] != '*':
                        return False
                return True
            
            # Recursive cases
            if p[j] == s[i] or p[j] == '?':  # Characters match or pattern is '?'
                memo[(i, j)] = helper(i - 1, j - 1)
            elif p[j] == '*':  # Pattern is '*', match zero or more characters
                memo[(i, j)] = helper(i, j - 1) or helper(i - 1, j)
            else:  # Characters don't match
                memo[(i, j)] = False
            
            return memo[(i, j)]
        
        return helper(l - 1, k - 1)
