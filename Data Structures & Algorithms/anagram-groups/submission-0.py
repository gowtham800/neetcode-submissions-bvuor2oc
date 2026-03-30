class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        hash_map = collections.defaultdict(list)

        for string in strs:
            counts = [0] * 26
            for ch in string:
                counts[ord(ch) - ord('a')] += 1
            hash_map[tuple(counts)].append(string)
        
        return list(hash_map.values())
        
        