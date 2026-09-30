class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> arr;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int left = i + 1;
            int right = n - 1;
            int total_sum = -1 * nums[i];
            while (left < right) {
                int total = nums[left] + nums[right];
                if (total == total_sum) {
                    arr.push_back({nums[left], nums[right], nums[i]});
                    left++;
                    right--;
                    while (left < n && nums[left] == nums[left - 1]) {
                        left++;
                    }
                    while (right >= 0 && nums[right] == nums[right + 1]) {
                        right--;
                    }
                }
                else {
                    if (total < total_sum) {
                        left++;
                    }
                    else {
                        right--;
                    }
                }
            }
        }
        return arr;
    }
};