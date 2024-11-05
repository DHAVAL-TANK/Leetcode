from typing import List
def cherryPicking(matrix: List[List[int]]) -> int:
    res = [[[0]*col for col in row] for row in matrix]
    n=len(matrix)
    m=len(matrix[0])

    for i in range(n-2,-1,-1):
        for j in range(m):
            res[i][j]= min(res[i+1][j-1] if j > 0 else float('inf'),
                            res[i+1][j] ,
                            res[i+1][j+1] if j < m-1 else float('inf')) + matrix[i][j]
    return min(res[0])
       

matrix = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
print(cherryPicking(matrix))