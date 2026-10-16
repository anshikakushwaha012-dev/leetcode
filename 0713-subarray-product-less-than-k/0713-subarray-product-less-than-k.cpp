class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
       int count=0;
       for(int i=0;i<nums.size();i++){
        long long product=1;
        for(int j=i;j<nums.size();j++){
            if(product >= k || product > (k-1)/nums[j]){
                break;
            }
            product=product*nums[j];
            count++;
        }
       }
       return count;
    }
};