from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)        # Number of rows
        n = len(image[0])     # Number of columns
        originalColor = image[sr][sc]

        # Optimization: If the original color is the same as the new color, no need to proceed
        if originalColor == color:
            return image

        def dfs(i: int, j: int):
            # Boundary checks: rows vs m and columns vs n
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != originalColor:
                return
            
            # Change the color
            image[i][j] = color

            # Explore all four directions
            dfs(i - 1, j)  # Up
            dfs(i + 1, j)  # Down
            dfs(i, j + 1)  # Right
            dfs(i, j - 1)  # Left

        # Start DFS from the initial cell
        dfs(sr, sc)

        return image

# 📌 **Example Usage**
if __name__ == "__main__":
    solution = Solution()
    image = [
        [1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,0,0]
    ]
    sr, sc, color = 1, 1, 2
    result = solution.floodFill(image, sr, sc, color)
    print("Flood Filled Image:")
    for row in result:
        print(row)
    # Expected Output:
    # [
    #   [2,2,2,2,0],
    #   [2,2,0,2,0],
    #   [2,2,0,0,0],
    #   [0,0,0,0,0]
    # ]
