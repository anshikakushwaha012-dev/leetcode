class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n=nums.size();
        k=k%n;
        vector<int>temp(n);
        int i=n-k;
        int j=0;
        for(i=n-k;i<n;i++){
            temp[j]=nums[i];
            j++;
        }
        for(i = 0; i < n-k; i++) {
            temp[j] = nums[i];
            j++;
        }
        for(i = 0; i < n; i++) {
            nums[i] = temp[i];
        }
    }
};