class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap2 = {}

        #initalizes hashmap for word s
        for letter in s:
            if letter not in hashmap:
                hashmap[letter] = 0
            hashmap[letter] += 1

        #initalizes hashmap2 for word t
        for letter in t:
            if letter not in hashmap2:
                hashmap2[letter] = 0
            hashmap2[letter] += 1

        #compare hashmap letter counts
        if hashmap == hashmap2:
            return True
        else:
            return False