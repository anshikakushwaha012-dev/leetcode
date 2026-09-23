class Solution:
    def maxArea(self, height: list[int]) -> int:
        n=len(height)
        maxarea=0
        ht=0
        left=0
        right=n-1
        while left<right:
            ht=min(height[left],height[right])
            width=right-left
            area=width*ht
            maxarea=max(maxarea,area)
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return maxarea