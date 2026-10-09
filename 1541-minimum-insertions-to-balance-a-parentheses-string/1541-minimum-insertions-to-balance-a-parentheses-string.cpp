class Solution {
public:
    int minInsertions(string s) {
        int ans=0;
        int left=0;
        int i=0;
        while (i<s.length()){
            if (s[i]=='('){
                left++;
            } else{
                if (i+1<s.length() && s[i+1]==')'){
                    left--;
                    i++;
                } else{
                    ans++;
                    left--;
                }
                if(left<0){
                    ans++;
                    left=0;
                }
            }
            i++;
        }
        ans+=left*2;
        return ans;
    }
};