def searchInsert(nums, target):
        
        start=0
        end=len(nums)-1
        
        if end+1==1:
            if nums[start]>=target:
                return 0
            else:
                return 1
            
        while start<=end:
            
            mid=(start+end)/2
            
            if nums[mid]==target:
                return mid
            
            elif nums[mid]<target:
                start=mid+1
            
            else:
                end=mid-1
        
        return start
        