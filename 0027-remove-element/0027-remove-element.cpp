class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count=0;
        int left=0;
        int right=nums.size()-1;
        while (left<=right){
            if (nums[left]==val){
                nums[left]=nums[right];
                right--;
            }
            else {
                left++;
                count++;
            }
        }
        return count;
    }
};