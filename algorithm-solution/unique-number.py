def singleNumber(nums):
        
        #XOR of same bits gives zero
        # ^ is the XOR operator in python
        
        a=0
        for i in nums:
            
            a^=i
        
        return a