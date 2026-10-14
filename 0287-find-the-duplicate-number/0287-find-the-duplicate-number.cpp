class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int answer=0;
        int ptr=0;
        for(int i=1;i<nums.size();i++){
            if(nums[i]==nums[ptr]){
                answer=nums[i];
            }
            ptr++;
        }
        return answer;
    }
};