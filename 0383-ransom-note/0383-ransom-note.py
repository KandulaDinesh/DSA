class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = {}
        
        # Count occurrences of each character in magazine
        for char in magazine:
            char_count[char] = char_count.get(char, 0) + 1

        # Check if there are enough occurrences of each character in magazine
        for char in ransomNote:
            if char_count.get(char, 0) == 0:
                return False
            char_count[char] -= 1

        return True
