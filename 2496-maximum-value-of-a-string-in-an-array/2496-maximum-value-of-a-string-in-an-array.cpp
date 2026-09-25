class Solution {
public:
    int maximumValue(vector<string>& strs) {
        int ans=0;
        for(string s:strs) {
            bool digit=true;
            for(char c:s) {
                if(c<'0' || c>'9') {
                    digit=false;
                    break;
                }
            }
            int value;
            if(digit){
                value=stoi(s);
            }
            else {
                value=s.length();
            }
            ans=max(ans, value);
        }
        return ans;
    }
};