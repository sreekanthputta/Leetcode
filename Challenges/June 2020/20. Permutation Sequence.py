class Solution:
    k = None
    factorial = {}
    def getPermutation(self, n: int, k: int) -> str:
        self.k = k
        return ''.join([str(x) for x in self.rec(n)])
        
    def rec(self, n, path = []):
        if(self.k>1):
            waysFact = self.fact(n-len(path)-1)
            index = int(self.k/waysFact)
            if(self.k % waysFact == 0):
                index -= 1
            self.k -= waysFact*index
            print(self.k, waysFact, index, [x for x in range(1, n+1) if x not in path])
            return self.rec(n, path+[[x for x in range(1, n+1) if x not in path][index]])
        else:
            return (path+[x for x in range(1, n+1) if x not in path])
            
    
    
    def fact(self, n):
        if(n in self.factorial):
            return self.factorial[n]
        if(n == 1):
            return 1
        else:
            self.factorial[n] = self.fact(n-1)*n
            return self.factorial[n]