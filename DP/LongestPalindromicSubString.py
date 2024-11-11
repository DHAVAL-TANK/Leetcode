def longest_palindrome(s: str) -> str:
    n = len(s)
    reversed_s = s[::-1]
    max_length = 0
    end_index_s = 0
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == reversed_s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if n - j == i - dp[i][j]:
                    max_length = dp[i][j]
                    end_index_s = i
            else:
                dp[i][j] = 0

    # Extract the longest palindromic substring
    if max_length > 0:
        start_index_s = end_index_s - max_length
        return s[start_index_s:end_index_s]

    return ""

