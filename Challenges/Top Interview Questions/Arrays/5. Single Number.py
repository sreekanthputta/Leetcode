class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        nums.sort()
        print(nums)
        if(nums[0]!=nums[1]):
            return nums[0]
        elif(nums[len(nums)-1]!=nums[len(nums)-2]):
            return nums[len(nums)-1]
        for i in range(1, len(nums)-1):
            if(nums[i-1]!=nums[i] and nums[i]!=nums[i+1]):
                return nums[i]