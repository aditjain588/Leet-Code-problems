class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if(k<=1):
            return 0
        start=0
        end=0
        pro=1
        count=0
        while(end<len(nums)):
            pro=pro*nums[end]
            while(pro>=k):
                pro=pro/nums[start]
                start+=1
            count+=end-start+1
            end+=1
            print(count)
        return(count)