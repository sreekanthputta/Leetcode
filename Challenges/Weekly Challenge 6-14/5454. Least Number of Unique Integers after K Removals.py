from collections import defaultdict
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = defaultdict(lambda : 0)
        for num in arr:
            freq[num] += 1
        sortedFreq = (sorted(freq.items(), key=lambda x : x[1], reverse = True))
        
        while(k>0):
            print ("k", k, sortedFreq[-1][1])
            if k>=sortedFreq[-1][1]:
                k -= sortedFreq[-1][1]
                del sortedFreq[-1]
            else:
                break
                
        return len(sortedFreq)