'''
#Time consuming - n! time
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(1, nums[0]+1):
            if(len(nums)<=nums[0]):
                return True
            canJumpBool = self.canJump(nums[i:])
            if(canJumpBool):
                return True
        return False
		

#Time - n^2
#-1 denotes that the element can reach the last index
#-2 denotes the opposite as -1
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums[len(nums)-1] = -1
        for index in range(len(nums)-2, -1,-1):
            nums[index]==-2
            i=1
            while(i<=nums[index]):
                if(nums[index+i]==-1):
                    nums[index]=-1
                    break;
                i+=1
        return nums[0]==-1
'''		

#Time - n (Accepted)
#-1 denotes that the element can reach the last index
#-2 denotes the opposite as -1
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        posNearIndex = len(nums)-1
        print(posNearIndex)
        for index in range(len(nums)-2, -1,-1):
            if(nums[index]>= posNearIndex-index):
                posNearIndex = index
        return posNearIndex==0