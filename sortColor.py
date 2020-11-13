class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #pointer i traversing the list, pointer start holding the next position for 0, pointer end holding the next position for 2
        # if 0 encountered put it in starting of list, if 2 encountered put it in ending of list, value 1 will automatically will be in the middle
        start=0
        end=len(nums)-1
        i=0
        
        while(i<=end):     
            if(nums[i]==0):
                nums[i],nums[start] = nums[start],nums[i]
                start+=1
                i+=1
            elif(nums[i]==2):
                nums[i],nums[end] = nums[end],nums[i]
                end-=1
            else:
                i+=1
            print(i)
