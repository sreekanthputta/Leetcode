class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if(len(nums)==1 and nums[0]<0):
            return nums[0]
        def prod(starti, endi):
            res = 0
            for i in range(starti, endi):
                print(starti, endi)
                if(res==0):
                    res = 1
                res*=nums[i]
            return res
        
        negPos = []
        zeroPos = [-1]
        for i, num in enumerate(nums):
            if(num==0):
                zeroPos.append(i)
            elif(num<0):
                negPos.append(i)
        zeroPos.append(len(nums))
        #print(zeroPos)
            
        maxProd = 0
        for zeroi in range(1, len(zeroPos)):
            negInPos = [x for x in negPos if x>zeroPos[zeroi-1] and x<zeroPos[zeroi]]
            #print(zeroi, negInPos)
            noOfNeg = len(negInPos)%2
            if(noOfNeg == 0):
                maxProd = max(maxProd, prod(zeroPos[zeroi-1]+1, zeroPos[zeroi])) 
            else:
                maxProd = max(maxProd, prod(zeroPos[zeroi-1]+1, negInPos[0]), prod(negInPos[0]+1, zeroPos[zeroi]), prod(zeroPos[zeroi-1]+1, negInPos[-1]), prod(negInPos[-1]+1, zeroPos[zeroi]))
                
        return (maxProd)