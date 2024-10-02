class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        
        # Create a rank dictionary, where each element gets a rank starting from 1
        rank_map = {num: i + 1 for i, num in enumerate(sorted_unique)}
        
        # Replace each element in the original array with its rank
        return [rank_map[num] for num in arr]