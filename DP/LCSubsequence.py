
def longestCommonSubsequence( text1: str, text2: str):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        lcs=""
        
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        i=l1
        j=l2
        while i>0 and j>0:
            if text1[i-1] == text2[j-1]:
                lcs+=text1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j] > dp[i][j-1]:
                i-=1
            else:
                j-=1
            
        print(lcs[::-1])
        return dp[l1][l2]

s1="abderfd"
s2="dflsabrfor"
print(longestCommonSubsequence(s1,s2))


