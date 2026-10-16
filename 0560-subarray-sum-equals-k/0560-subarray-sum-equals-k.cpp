class Solution {
public:
    int subarraySum(vector<int>& nums, int k){
        unordered_map<int,int>mp;
        int n=nums.size();
        int count=0;
        int sum=0;
        mp[0]=1; 
        for(int i=0;i<n;i++){
            sum+=nums[i];
            int prev=sum-k;
            if(mp.find(prev)!=mp.end()){
                count=count+mp[prev];
            }
            mp[sum]++;
        }
        return count;
    }
};