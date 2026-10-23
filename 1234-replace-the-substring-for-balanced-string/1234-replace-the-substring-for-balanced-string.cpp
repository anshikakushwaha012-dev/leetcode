class Solution {
public:
    int balancedString(string s) {
        int n=s.length();
        int k=n/4;
        unordered_map<char,int>count;
        for (char c:s){
            count[c]++;
        }
        if (count['Q']==k && count['W']==k &&
            count['E']==k && count['R']==k){
            return 0;
        }
        int left=0,ans=n;
        for (int right=0;right<n;right++){
            count[s[right]]--;
            while (count['Q']<=k && count['W']<=k &&
                   count['E']<=k && count['R']<=k){
                ans=min(ans,right-left+1);
                count[s[left]]++;
                left++;
            }
        }
        return ans;
    }
};