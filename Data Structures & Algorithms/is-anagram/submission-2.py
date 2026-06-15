class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lengthS = len(s)
        lengthT = len(t)

        if lengthS != lengthT:
            return False
        
        alphabet = [0] * 26

        for i in range(lengthS):
            alphabet[ord(s[i]) - ord('a')] += 1
            alphabet[ord(t[i]) - ord('a')] -= 1
        
        return not any(alphabet)