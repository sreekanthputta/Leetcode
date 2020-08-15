O(n^2) solution:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        map = {}
        ansSet = set()
        for i, num in enumerate(nums):
            if(num in map):
                map[num].append(i)
            else:
                map[num] = [i]

        for i, first in enumerate(nums):
            for j, second in enumerate(nums[i+1:], i+1):
                indices = map[-first-second] if (-first-second) in map else None
                if(indices!=None):
                    third = list(filter(lambda x : x>j, indices))
                    if(len(third)>0):
                        ans = [first, second, nums[third[0]]]
                        ans.sort()
                        print(ans)
                        ansSet.add(','.join([str(x) for x in ans]))
                    # print(first, second, list(filter(lambda x : x>j, indices)))
        return [[int(y) for y in x.split(',')] for x in ansSet]