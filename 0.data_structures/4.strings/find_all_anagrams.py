class Solution:
    
    def makeCounter(self, s):
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1
        return d
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counterP = self.makeCounter(p)
        counterI = self.makeCounter(s[:len(p)])
        result = []
        for i in range(0, len(s)-len(p)+1):
            if counterP == counterI:
                result.append(i)
            counterI[s[i]] -= 1
            if counterI[s[i]] == 0:
                del counterI[s[i]]
            if i + len(p) < len(s):
                counterI[s[i+len(p)]] = counterI.get(s[i+len(p)], 0) + 1 
        return result
