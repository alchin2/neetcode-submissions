from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1) 
        curr = Counter() 
        left = 0

        for right, char in enumerate(s2):
            curr[char] += 1

            while curr[char] > need[char]:
                curr[s2[left]] -= 1
                left += 1

            if right - left + 1 == len(s1):
                return True

        return False
