class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxarea=0
        while(i<j):
            maxarea=max(((j-i)*min(height[i],height[j])),maxarea)
            if(height[i]<height[j]):
                i=i+1
            else:
                j=j-1
        return(maxarea)