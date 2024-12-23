def canYouMake(s1: str, s2: str) -> int:
    l1 = len(s1)
    l2 = len(s2)

    dp = [[0] * (l2+1) for _ in range(0,l1+1)]

    for i in range(1,l1+1):
        for j in range (1,l2+1):
            if s1[i-1] == s2 [j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
    return l1+l2 - (2 * dp[l1][l2])