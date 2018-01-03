class Solution(object):
    def removeDuplicates(self, nums):
        
        if len(nums)==0:
            return 0

        
        i=0
        while 1>0:
            if len(nums)-1 == i:
                break
            if nums[i]==nums[i+1]:
                del nums[i]
                i=nums.index(nums[i])
            else:
                i+=1
            
        return len(nums)