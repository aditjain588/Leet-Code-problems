class Solution:
    def findPairs(self, nums: List[int], k: int) -> int: 
        c=Counter(nums)
        count=0
        for key,v in c.items():
            if(k==0):
                if(v>1):
                    count=count+1
            elif(key + k) in c:
                count+=1
                
        return count
                