class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_mapping_s = {}
        char_mapping_t = {}

        for char_s, char_t in zip(s, t):
            # Check mapping in s
            if char_s in char_mapping_s:
                if char_mapping_s[char_s] != char_t:
                    return False
            else:
                char_mapping_s[char_s] = char_t

            # Check mapping in t
            if char_t in char_mapping_t:
                if char_mapping_t[char_t] != char_s:
                    return False
            else:
                char_mapping_t[char_t] = char_s

        return True
