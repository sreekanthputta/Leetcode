class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort(reverse = True)
        median = arr[(int)((len(arr))/2)]
        arr.sort(key = lambda x : abs(x-median), reverse = True)
        return arr[:k]