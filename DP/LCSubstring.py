
def longestCommonSubstring( text1: str, text2: str):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        lcs=""
        max=0
        maxi=0
        maxj=0
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    if dp[i][j] >= max:
                        max = dp[i][j]
                        maxi = i
                        maxj=j
                else:
                    dp[i][j] = 0
        i=maxi
        j=maxj
        while dp[i][j] > 0:
            if text1[i-1] == text2[j-1]:
                lcs+=text1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j] > dp[i][j-1]:
                i-=1
            else:
                j-=1
            
        print(lcs[::-1])
        return max

s1="abcderfd"
s2="dflsabcrfor"
print(longestCommonSubstring(s1,s2))


