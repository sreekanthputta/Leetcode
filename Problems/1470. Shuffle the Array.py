class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first = nums[:n]
        del nums[:n]
        for i, num in enumerate(first):
            nums.insert((i)*2, num)
        return (nums)