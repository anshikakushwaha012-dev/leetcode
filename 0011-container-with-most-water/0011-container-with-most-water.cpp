class Solution {
public:
    int maxArea(vector<int>& height) {
        int n=height.size();
        int left=0;
        int right=n-1;
        int maxarea=0;
        int ht=0;
        int width=0;
        int area=0;
        while(left<right){
            ht=min(height[left],height[right]);
            width=right-left;
            area=width*ht;
            maxarea=max(maxarea,area);
            if(height[left]<height[right]){
                left++;
            }
            else{
                right--;
            }
            }
            return maxarea;
        }
    
};