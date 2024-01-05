class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        hashmapS,hashmapT={},{}

        for char in range(len(s)):
            hashmapS[s[char]]=1+hashmapS.get(s[char],0)
            hashmapT[t[char]]=1+hashmapT.get(t[char],0)
        for i in hashmapS:
            if hashmapS[i] != hashmapT.get(i,0):
                return False
        return True