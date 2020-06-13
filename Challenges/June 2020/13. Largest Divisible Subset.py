from collections import defaultdict
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        knownSet = defaultdict(lambda : [])
        maxSubset = None
        for i, num in enumerate(nums):
            maxFactors = None
            for n in nums[:i]:
                if(num % n == 0 and len(knownSet[n])>=len(knownSet[maxFactors])):
                    maxFactors = n
            if(maxFactors != None):
                knownSet[num] = knownSet[maxFactors]+[maxFactors]
            maxSubset = num if len(knownSet[num]) > len(knownSet[maxSubset]) else maxSubset
                
        if(maxSubset==None):
            if(len(nums)==0):
                return []
            else:
                return [nums[0]]
        else:
            return knownSet[maxSubset]+[maxSubset]