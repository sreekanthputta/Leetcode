class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        aMarker = 0
        bMarker = 0 
        tLength = len(t)
        sLength = len(s)
        while(bMarker < tLength and aMarker < sLength):
            if(s[aMarker] == t[bMarker]):
                aMarker+=1
            bMarker+=1
        return aMarker == sLength