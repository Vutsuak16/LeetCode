class Solution(object):
    def searchRange(self, nums, target):
        
        if len(nums)==0:
            return [-1,-1]
        if nums[0]==target and nums[-1]==target:
            return [0,len(nums)-1]
        
        start=0
        end=len(nums)-1
        a=-1
        b=-1
        
        while start<=end:
            mid= (start+end)/2
            if mid ==0 and nums[mid]==target:
                a=mid
                break
            if nums[mid]==target and nums[mid-1]<target :
                a=mid
                break
            elif nums[mid]>=target:
                end=mid-1
            else:
                start=mid+1
        print a
        start=0
        end=len(nums)-1
        
        while start<=end:
            mid= (start+end)/2
            if mid==len(nums)-1 and nums[mid]==target:
                b=mid
                break
            if nums[mid]==target and nums[mid+1]>target:
                b=mid
                break
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        if a==-1 and b==-1:
            return [-1,-1]
        else:
            return [a,b]
        
            