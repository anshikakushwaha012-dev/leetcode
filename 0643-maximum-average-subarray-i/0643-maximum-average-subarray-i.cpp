class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n=nums.size();
        int maxsum=INT_MIN;
        int sum=0;
        int start=0;
        for(int end=0;end<n;end++){
            sum+=nums[end];
            if(end>=k-1){
                maxsum=max(maxsum,sum);
                sum-=nums[start];
                start++;
            }
        }
        return double(maxsum)/k;
    }
};