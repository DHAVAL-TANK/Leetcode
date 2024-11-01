from typing import List
# https://leetcode.com/problems/triangle/submissions/1440295456/
# def minimumTotal(triangle: List[List[int]]) -> int:
#     dp=[[0 for  _ in row] for row in triangle]
#     print(dp)
#     dp[0][0]=triangle[0][0]
#     for row in range(1,len(triangle)):
#         for col in range(len(triangle[row])):
#             print(row,col,triangle[row][col])
#             if col==0 :
#                 dp[row][col]=dp[row-1][col]+triangle[row][col]
#             elif col == len(triangle[row])-1:
#                 dp[row][col]=dp[row-1][col-1]+triangle[row][col]
#             else:
#                 dp[row][col]= min(dp[row-1][col-1] , dp[row-1][col])+triangle[row][col] 
#     return min(dp[-1]) 

def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        res = triangle
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                res[i][j] = min(res[i+1][j], res[i+1][j+1]) + triangle[i][j]
        
        return res[0][0]

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(triangle))