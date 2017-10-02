def threeSum(nums):
        
        lists=[]
        nums=sorted(nums)
        length=len(nums)
        for i in range(len(nums)-1):
                l=i+1
                r=length-1
                while l<r:
                    if nums[i]+nums[l]+nums[r]==0 and [nums[i],nums[l],nums[r]] not in lists:
                        lists.append([nums[i],nums[l],nums[r]])
                        r-=1
                        l+=1
                    elif nums[i]+nums[l]+nums[r]<0:
                        l+=1
                    else: r-=1
               
        return lists