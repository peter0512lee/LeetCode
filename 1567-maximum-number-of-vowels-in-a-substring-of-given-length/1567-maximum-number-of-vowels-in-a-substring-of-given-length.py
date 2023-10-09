class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        lib = {'a' , 'e' , 'i' , 'o' , 'u'}
        max_vowel = 0
        curr_vowel = 0
        for i in range(k) :
            if s[i] in lib :
                curr_vowel += 1
        max_vowel = curr_vowel
        for i in range(k , len(s)) :
            if s[i - k] in lib :
                curr_vowel -= 1
            if s[i] in lib :
                curr_vowel += 1
            max_vowel = max(curr_vowel , max_vowel )
        return max_vowel 