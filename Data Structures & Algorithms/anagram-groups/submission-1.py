class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}
        for word in strs:
            key = {}
            for char in word:
                key[char] = key.get(char, 0) + 1
            key = tuple(sorted(key.items())) # must be sorted to prevent unique key for group anagrams
            group_anagrams.setdefault(key, []).append(word) # return the reference of the list to append to
        return list(group_anagrams.values())