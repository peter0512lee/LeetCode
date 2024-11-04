class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
        return ""

        comp = []
        i = 0
        n = len(word)

        while i < n:
            # Get current character
            curr_char = word[i]

            # Count consecutive occurrences, but not more than 9
            count = 1
            j = i + 1
            while j < n and word[j] == curr_char and count < 9:
                count += 1
                j += 1

            # Append count and character to result
            comp.append(str(count))
            comp.append(curr_char)

            # Move index to next different character
            i = j

        return "".join(comp)