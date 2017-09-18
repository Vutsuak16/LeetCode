def removeElement(nums, val):
        
        i=0
        while  1>0:
            
            if val not in nums:
                break
                
            if nums[i]==val:
                del(nums[i])
                continue
            
            i+=1
        
        return len(nums)


 # use while loop in case of index prob iterate and continue are useful

 