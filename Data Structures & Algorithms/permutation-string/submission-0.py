from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        char_frequency = Counter(s1)
        length = len(s1)

        r = length - 1

        while r <= len(s2):
            if char_frequency == Counter(s2[l:r+1]):
                return True
            
            r += 1
            l += 1

        return False

