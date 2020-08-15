class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, num in enumerate(nums):
            if(num in numDict and i!=numDict[num]):
                return [i, numDict[num]]
            else:
                numDict[target - num] = i