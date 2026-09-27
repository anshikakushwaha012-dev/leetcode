class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int richest=0;
        for(auto i:accounts) {
            int wealth=0;
            for(int j:i) {
                wealth+=j;
            }
            richest=max(richest,wealth);
        }
        return richest;
    }
};