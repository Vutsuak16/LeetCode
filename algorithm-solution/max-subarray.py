def maxSubArray(self, nums):
        
        maxint= -1 * (2**31-1)
        currmax=0
        
        for i in nums:
          
            currmax+=i
            if currmax>maxint:
                maxint=currmax
        
        
            if currmax<0:
                currmax=0
        
        return maxint
            