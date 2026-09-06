class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            if str(sorted(word)) not in hashmap:
                hashmap[str(sorted(word))] = [word]
            else:
                hashmap[str(sorted(word))].append(word)

        anagram_strs = []
        for value in hashmap.values():
            anagram_strs.append(value)
        return anagram_strs
                        