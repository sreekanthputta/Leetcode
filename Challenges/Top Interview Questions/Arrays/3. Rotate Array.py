class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        first = nums[:length-k]
        del nums[:length-k]
        nums.extend(first)