class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int missing=-1;
        int duplicate=-1;
        int n=nums.size();

        for(int i=1;i<=n;i++){
            int count=0;

            for(int j=0;j<n;j++){
                if(nums[j]==i){
                    count++;
                }
            }

            if(count==0)
                missing=i;

            if(count==2)
                duplicate=i;
        }

        return {duplicate,missing};
    }
};