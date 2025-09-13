class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_dict = {'a': 0, 'e': 0, 'i':0, 'o':0, 'u':0}
        consonant_dict = dict()
        for char in s:
            if char in vowel_dict:
                vowel_dict[char] += 1
            else:
                if char not in consonant_dict:
                    consonant_dict[char] = 0
                consonant_dict[char] += 1
        if not consonant_dict:
            return max(vowel_dict.values())
        return max(vowel_dict.values()) + max(consonant_dict.values())