'''
 Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice. '''

def twoSum(self, nums, target):
        
        l=[]
        for i in nums:
            for j in range(nums.index(i)+1,len(nums)):
                if i + nums[j] == target:
                    l.append(j)
                    l.append(nums.index(i))
                    return sorted(l)