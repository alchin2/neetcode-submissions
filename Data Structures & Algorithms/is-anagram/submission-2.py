class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = {}
        set2 = {}
        set1 = {}
        for char in s:
            set1[char] = set1.get(char, 0) + 1

        for char in t:
            set2[char] = set2.get(char, 0) + 1
    

        return set1==set2