class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)
        for i, c in enumerate(s[:(int)(length/2)]):
            temp = s[length-1-i]
            s[length-1-i] = s[i]
            s[i] = temp