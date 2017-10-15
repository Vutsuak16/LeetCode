class Solution(object):
    def removeDuplicates(self, nums):
       
        start=0
        end=len(nums)-1
        length=len(nums)
        if start==end:
            return len(nums)
        while start<end:
            if nums[start+1]==nums[start]:
                length-=1
                nums.remove(nums[start])
                if start!=0:
                    start-=1
            else:
                start+=1
            end=len(nums)-1
        print nums
        return length
    