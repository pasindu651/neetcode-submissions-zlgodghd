class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagrams = {}
        for s in strs:
            count = {}
            for c in s:
                count[c] = count.get(c, 0) + 1
            count = tuple(sorted(count.items())) # sort by alphabetical order to prevent unique keys for different order of characters
            groupAnagrams.setdefault(count, []).append(s)
        print(groupAnagrams)
        return [value for key,value in groupAnagrams.items()]