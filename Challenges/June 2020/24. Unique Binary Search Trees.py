import math
class Solution:
    def numTrees(self, n: int) -> int:
        memoisedResult = {0:1}
        for numOfNodes in range(1, n+1):
            sum = 0
            for i in range(1, math.floor((numOfNodes)/2)+1):
                sum += (memoisedResult[i - 1] * memoisedResult[numOfNodes - i]) * 2
            if(numOfNodes%2 != 0):
                sum += memoisedResult[math.floor(numOfNodes/2)]**2
            memoisedResult[numOfNodes] = sum
        print(memoisedResult)
        return memoisedResult[n]