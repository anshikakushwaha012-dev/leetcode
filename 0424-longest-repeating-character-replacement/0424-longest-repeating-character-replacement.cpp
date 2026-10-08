class Solution {
public:
    int characterReplacement(string s, int k) {
        int low=0;
        int high=0;
        int n=s.length();
        int maxFreq=0;
        int ans=0;
        unordered_map<char, int> f;
        for (high=0;high<n;high++){
            f[s[high]]++;
            maxFreq=max(maxFreq,f[s[high]]);
            int window=high-low+1;
            if(window-maxFreq>k){
                f[s[low]]--;
                low++;
            }
            ans=max(ans,high-low+1);
        }
        return ans;
    }
};