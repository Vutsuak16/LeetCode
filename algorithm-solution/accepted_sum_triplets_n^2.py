def threeSum(nums):
        
        if len(nums)<3:
            return []
        if len(nums)==nums.count(0):
            return [[0]*3]
        lists=[]
        nums=sorted(nums)
        length=len(nums)
        k=set()
        for i in range(len(nums)-1):
                l=i+1
                r=length-1
                while l<r:
                    if nums[i]+nums[l]+nums[r]==0 :
                        k.add((nums[i],nums[l],nums[r]))
                        r-=1
                        l+=1
                    elif nums[i]+nums[l]+nums[r]<0:
                        l+=1
                    else: r-=1
        
        
       
            
        return [list(i) for i in k ]




#tuples can be added to set
#using set to eliminate duplicates
#removing many zeros error as well
