from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colors = defaultdict(lambda : 0)
        for num in nums:
            colors[num]+=1
        nums.clear()
        nums.extend([0]*colors[0]+[1]*colors[1]+[2]*colors[2])