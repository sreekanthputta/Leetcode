class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(len(nums)<=1):
            return False
        noDupList = {nums[0]}
        for num in nums[1:]:
            noDupList.add(num)
        return len(noDupList)!=len(nums)