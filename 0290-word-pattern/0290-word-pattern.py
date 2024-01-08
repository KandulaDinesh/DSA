class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping_char_word = {}
        mapping_word_char = {}

        for char, word in zip(pattern, words):
            if char in mapping_char_word:
                if mapping_char_word[char] != word:
                    return False
            else:
                mapping_char_word[char] = word

            if word in mapping_word_char:
                if mapping_word_char[word] != char:
                    return False
            else:
                mapping_word_char[word] = char

        return True
