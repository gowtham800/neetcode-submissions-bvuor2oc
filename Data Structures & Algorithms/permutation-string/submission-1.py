class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for i in range(m):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        matches = sum(1 for i in range(26) if s1_count[i] == window_count[i])

        if matches == 26:
            return True

        for r in range(m, n):
            l = r - m

            idx_add = ord(s2[r]) - ord('a')
            window_count[idx_add] += 1
            if window_count[idx_add] == s1_count[idx_add]:
                matches += 1
            elif window_count[idx_add] == s1_count[idx_add] + 1:
                matches -= 1

            idx_rem = ord(s2[l]) - ord('a')
            window_count[idx_rem] -= 1
            if window_count[idx_rem] == s1_count[idx_rem]:
                matches += 1
            elif window_count[idx_rem] == s1_count[idx_rem] - 1:
                matches -= 1 

            if matches == 26:
                return True

        return False