class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26

        for ch in s:
            counts[ord(ch) - ord('a')] += 1

        for ch in t:
            counts[ord(ch) - ord('a')] -= 1

        for c in counts:
            if c != 0:
                return False

        return True
       

