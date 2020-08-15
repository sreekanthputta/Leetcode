class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor^= num
        lowBit = xor&-xor
        bit1XOR = 0
        bit2XOR = 0
        for num in nums:
            if(lowBit & num == lowBit):
                bit1XOR ^= num
            else:
                bit2XOR ^= num
        return [bit1XOR, bit2XOR]