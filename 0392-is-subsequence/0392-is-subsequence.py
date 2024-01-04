class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True  # An empty string is always a subsequence

        s_pointer, t_pointer = 0, 0

        while t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                if s_pointer == len(s):
                    return True  # All characters in s are found in t
            t_pointer += 1

        return False
