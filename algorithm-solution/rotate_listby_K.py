
def rotate(nums, k):
        
        if len(nums)==1 or k==0:
            nums=nums
        else:
            if k>len(nums):
                k= k%len(nums)
            index={}
            for i in range(len(nums)):
                if i+k>=len(nums):
                    index[i+k - len(nums)]=nums[i]
                else:
                    index[i+k]=nums[i]

            for i in range(len(nums)):
                nums[i]=index[i]
            print nums