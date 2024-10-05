from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        
        if len_s1 > len_s2:
            return False
        
        # Frequency of characters in s1
        s1_count = Counter(s1)
        
        # Initial frequency of the first window in s2
        window_count = Counter(s2[:len_s1])
        
        # Check the first window
        if s1_count == window_count:
            return True
        
        # Sliding window over s2
        for i in range(len_s1, len_s2):
            # Add the next character in the window
            window_count[s2[i]] += 1
            # Remove the leftmost character from the window
            window_count[s2[i - len_s1]] -= 1
            
            # If the count becomes 0, we remove it from the dictionary
            if window_count[s2[i - len_s1]] == 0:
                del window_count[s2[i - len_s1]]
            
            # Check if the current window matches s1's frequency count
            if s1_count == window_count:
                return True
        
        return False
        
        