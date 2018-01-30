import random
from functools import reduce
class Solution:
    def permute(self, nums):
        if len(nums)==0:
            return None
        if len (nums)==1:
            return [[(nums[0])]]
        fact=reduce(lambda x,y: x*y,range(1,len(nums)+1))
        ct=0
        l=[]
        while True:
            if ct==fact:
                break
            k=[random.randrange(0,len(nums)) for i in range(len(nums))]
            if len(k) != len(set(k)):
                continue
            if k not in l:
                ct+=1
                l.append(k)
            else:
                continue
        ans=[]
        for i in l:
            ans.append([nums[j] for j in i])
        return ans
            
        