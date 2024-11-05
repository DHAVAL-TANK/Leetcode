from typing import List
def fallingPath(matrix: List[List[int]]) -> int:
    res=matrix
    n=len(matrix)
    m=len(matrix[0])

    for i in range(n-2,-1,-1):
        for j in range(m):
            res[i][j]= min(res[i+1][j-1] if j > 0 else float('inf'),
                            res[i+1][j] ,
                            res[i+1][j+1] if j < m-1 else float('inf')) + matrix[i][j]
    return min(res[0])
       

matrix = [[2,1,3],[6,5,4],[7,8,9]]
print(fallingPath(matrix))