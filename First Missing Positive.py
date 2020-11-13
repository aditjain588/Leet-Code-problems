class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if(nums==[]):
            return 1
        nums = list(filter(lambda x : x > 0, nums))
        if(nums==[]):
            return 1
        min_ele = min(nums)
        max_ele = max(nums)
        if(min_ele !=1):
            return 1
        elif(min_ele==1):
            for j in range(min_ele,max_ele):
                if(j not in nums):
                    return j
        
        c=max_ele+1
        return(c)
        