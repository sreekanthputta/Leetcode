class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        marker = 1
        for i, num in enumerate(nums[1:]):
            if(num != nums[i]):
                nums[marker] = num
                marker+=1
        return marker