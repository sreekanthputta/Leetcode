import random

class Solution:
    
    w = None
    deno = None
    def __init__(self, w: List[int]):
        self.w = w
        self.deno = sum(w)
        print(self.deno)

    def pickIndex(self) -> int:
        #print (random.randint(0,len(self.indices)-1))
        return (self.getIndex(random.randint(0,self.deno-1)))
    
    def getIndex(self, index) -> int:
        W = self.w
        for i,w in enumerate(W):
            index -= w
            if(index<0):
                return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()